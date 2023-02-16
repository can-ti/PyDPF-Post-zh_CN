"""Module containing the ``Simulation`` class."""
from abc import ABC, abstractmethod
from enum import Enum
import re
from typing import List, Tuple, Union

from ansys.dpf.core import DataSources, Model
from ansys.dpf.core.plotter import DpfPlotter
import numpy as np

from ansys.dpf import core
from ansys.dpf.post.mesh import Mesh
from ansys.dpf.post.selection import Selection


class ResultCategory(Enum):
    """Enum for available result categories."""

    scalar = 1
    vector = 2
    matrix = 3
    principal = 4
    equivalent = 5


class Simulation(ABC):
    """Base class of all PyDPF-Post simulation types."""

    _component_to_id = {
        "1": 0,
        "2": 1,
        "3": 2,
        "4": 3,
        "5": 4,
        "6": 5,
        "X": 0,
        "Y": 1,
        "Z": 2,
        "XY": 3,
        "YZ": 4,
        "XZ": 5,
    }

    _component_names = ["X", "Y", "Z", "XX", "XY", "YZ"]
    _principal_names = ["1", "2", "3"]

    def __init__(self, data_sources: DataSources, model: Model):
        """Initialize the simulation using a ``dpf.core.Model`` object."""
        self._model = model
        self._data_sources = data_sources
        self._geometries = []
        self._boundary_conditions = []
        self._loads = []
        self._active_selection = None
        self._named_selections = None
        self._mesh = None
        self._units = {
            "time/frequency": self.time_freq_support.time_frequencies.unit,
            "distance": self._model.metadata.meshed_region.unit,
        }
        self._time_freq_precision = None

    @property
    def results(self) -> List[str]:
        r"""Available results.

        Returns a list of available results as strings.

        Examples
        --------
        >>> from ansys.dpf import post
        >>> from ansys.dpf.post import examples
        >>> simulation = post.load_simulation(examples.static_rst)
        >>> print(simulation.results) # doctest: +NORMALIZE_WHITESPACE +ELLIPSIS
        ['displacement\nOperator name: "U"\n...Units: degc\n']
        """
        return [
            str(result) for result in self._model.metadata.result_info.available_results
        ]

    @property
    def geometries(self):
        """List of constructed geometries in the simulation.

        Returns a list of geometry objects.

        Examples
        --------
        >>> from ansys.dpf import post
        >>> from ansys.dpf.post import examples
        >>> simulation = post.load_simulation(examples.static_rst)
        >>> print(simulation.geometries) # doctest: +NORMALIZE_WHITESPACE +ELLIPSIS
        []
        """
        return self._geometries

    @property
    def boundary_conditions(self):
        """List of boundary conditions in the simulation.

        Returns a list of boundary_condition objects.

        Examples
        --------
        >>> from ansys.dpf import post
        >>> from ansys.dpf.post import examples
        >>> simulation = post.load_simulation(examples.static_rst)
        >>> print(simulation.boundary_conditions) # doctest: +NORMALIZE_WHITESPACE +ELLIPSIS
        []
        """
        return self._boundary_conditions

    @property
    def loads(self):
        """List of loads in the simulation.

        Returns a list of load objects.

        Examples
        --------
        >>> from ansys.dpf import post
        >>> from ansys.dpf.post import examples
        >>> simulation = post.load_simulation(examples.static_rst)
        >>> print(simulation.loads) # doctest: +NORMALIZE_WHITESPACE +ELLIPSIS
        []
        """
        return self._loads

    @property
    def mesh(self) -> Mesh:
        """Mesh representation of the model.

        Returns a :class:`ansys.dpf.post.mesh.Mesh` object.

        Examples
        --------
        >>> from ansys.dpf import post
        >>> from ansys.dpf.post import examples
        >>> simulation = post.load_simulation(examples.static_rst)
        >>> print(simulation.mesh) # doctest: +NORMALIZE_WHITESPACE +ELLIPSIS
        <ansys.dpf.post.mesh.Mesh object at ...>
        """
        if self._mesh is None:
            self._mesh = Mesh(self._model.metadata.meshed_region)
        return self._mesh

    @property
    def named_selections(self) -> List[str]:
        """List of named selections in the simulation.

        Returns a list of named selections names.

        Examples
        --------
        >>> from ansys.dpf import post
        >>> from ansys.dpf.post import examples
        >>> simulation = post.load_simulation(examples.static_rst)
        >>> print(simulation.named_selections) # doctest: +NORMALIZE_WHITESPACE +ELLIPSIS
        ['_FIXEDSU']
        """
        if self._named_selections is None:
            self._named_selections = self._model.metadata.available_named_selections
        return self._named_selections

    def plot(
        self,
        mesh: bool = True,
        constructed_geometries: bool = True,
        loads: bool = True,
        boundary_conditions: bool = True,
    ):
        """General plot of the simulation object.

        Plots by default the complete mesh contained in the simulation,
        as well as a representation of the constructed geometry,
        the loads, and the boundary conditions currently defined.
        Each representation can be deactivated with its respective boolean argument.

        Args:
            mesh:
                Whether to plot the mesh representation.
            constructed_geometries:
                Whether to plot the constructed geometries.
            loads:
                Whether to plot the loads.
            boundary_conditions:
                Whether to plot the boundary conditions.

        Returns
        -------
            Returns a plotter instance of the active visualization backend.

        Examples
        --------
        >>> from ansys.dpf import post
        >>> from ansys.dpf.post import examples
        >>> simulation = post.load_simulation(examples.static_rst)
        >>> simulation.plot() # doctest: +NORMALIZE_WHITESPACE +ELLIPSIS
        """
        plt = DpfPlotter()
        if mesh:
            plt.add_mesh(self.mesh._meshed_region)
        if constructed_geometries:
            for geom in self.geometries:
                getattr(plt, "add_" + str(type(geom).__name__).lower())(geom)
        if loads:
            pass
        if boundary_conditions:
            pass
        plt.show_figure()

    @property
    def active_selection(self) -> Selection:
        """Active selection used by default for result queries.

        Returns a :object:`ansys.dpf.post.selection.Selection` object.

        Examples
        --------
        >>> from ansys.dpf import post
        >>> from ansys.dpf.post import examples
        >>> simulation = post.load_simulation(examples.static_rst)
        >>> selection = post.selection.Selection()
        >>> simulation.activate_selection(selection=selection)
        >>> print(simulation.active_selection) # doctest: +NORMALIZE_WHITESPACE +ELLIPSIS
        <ansys.dpf.post.selection.Selection object at ...>
        """
        return self._active_selection

    def activate_selection(self, selection: Selection):
        """Sets a selection as active on the simulation.

        Activating a given selection on a simulation means it is used
        as a default selection/filter in further result queries.

        Examples
        --------
        >>> from ansys.dpf import post
        >>> from ansys.dpf.post import examples
        >>> simulation = post.load_simulation(examples.static_rst)
        >>> selection = post.selection.Selection()
        >>> simulation.activate_selection(selection=selection)
        >>> print(simulation.active_selection) # doctest: +NORMALIZE_WHITESPACE +ELLIPSIS
        <ansys.dpf.post.selection.Selection object at ...>
        """
        self._active_selection = selection

    def deactivate_selection(self):
        """Deactivate the currently active selection.

        Examples
        --------
        >>> from ansys.dpf import post
        >>> from ansys.dpf.post import examples
        >>> simulation = post.load_simulation(examples.static_rst)
        >>> selection = post.selection.Selection()
        >>> simulation.activate_selection(selection=selection)
        >>> print(simulation.active_selection) # doctest: +NORMALIZE_WHITESPACE +ELLIPSIS
        <ansys.dpf.post.selection.Selection object at ...>
        >>> simulation.deactivate_selection()
        >>> print(simulation.active_selection) # doctest: +NORMALIZE_WHITESPACE +ELLIPSIS
        None
        """
        self._active_selection = None

    @property
    def _time_frequencies(self):
        """Description of the temporal/frequency analysis of the model."""
        return self._model.metadata.time_freq_support

    @property
    def _get_time_freq_precision(self):
        """Computes a precision for times/frequencies requests based on the underlying support."""
        if self._time_freq_precision is None:
            available_values = self.time_freq_support.time_frequencies.data
            diff = np.diff(available_values, prepend=available_values[0] - 1.0)
            minimum = np.min(diff)
            self._time_freq_precision = minimum / 20.0
        return self._time_freq_precision

    @property
    def time_freq_support(self):
        """Description of the temporal/frequency analysis of the model."""
        return self._time_frequencies

    @property
    def units(self):
        """Returns the current time/frequency and distance units used."""
        return self._units

    def __str__(self):
        """Get the string representation of this class."""
        txt = (
            "%s." % re.sub(r"(?<!^)(?=[A-Z])", " ", type(self).__name__)
            + "\n\n\nData Sources\n------------------------------\n"
        )
        ds_str = self._model._data_sources.__str__()
        txt += ds_str
        txt += "\n\n"
        txt += self._model.__str__()
        return txt

    def _build_components_from_components(self, base_name, category, components):
        # Create operator internal names based on components
        out = []
        if components is None:
            out = None
        else:
            if isinstance(components, int) or isinstance(components, str):
                components = [components]
            if not isinstance(components, list):
                raise ValueError(
                    "Argument 'components' must be an int, a str, or a list of either."
                )
            for comp in components:
                if not (isinstance(comp, str) or isinstance(comp, int)):
                    raise ValueError(
                        "Argument 'components' can only contain integers and/or strings."
                    )
                if isinstance(comp, int):
                    comp = str(comp)
                if comp not in self._component_to_id.keys():
                    raise ValueError(
                        f"Component {comp} is not valid. Please use one of: "
                        f"{list(self._component_to_id.keys())}."
                    )
                out.append(self._component_to_id[comp])

        # Take unique values and build names list
        if out is not None:
            out = list(set(out))
        if out is None and category == ResultCategory.vector:
            columns = [base_name + comp for comp in self._component_names[:3]]
        elif out is None and category == ResultCategory.matrix:
            columns = [base_name + comp for comp in self._component_names]
        else:
            columns = [base_name + self._component_names[i] for i in out]
        return out, columns

    def _build_components_from_principal(self, base_name, components):
        # Create operator internal names based on principal components
        out = []
        if components is None:
            out = None
        else:
            if isinstance(components, int) or isinstance(components, str):
                components = [components]
            if not isinstance(components, list):
                raise ValueError(
                    "Argument 'components' must be an int, a str, or a list of either."
                )
            for comp in components:
                if not (isinstance(comp, str) or isinstance(comp, int)):
                    raise ValueError(
                        "Argument 'components' can only contain integers and/or strings."
                    )
                if str(comp) not in self._principal_names:
                    raise ValueError(
                        "A principal component ID must be one of: "
                        f"{self._principal_names}."
                    )
                out.append(comp - 1)

        # Take unique values
        if out is not None:
            out = list(set(out))
        # Build columns names
        if out is None:
            columns = [base_name + str(comp) for comp in self._principal_names]
        else:
            columns = [base_name + self._principal_names[i] for i in out]
        return out, columns

    @abstractmethod
    def _build_mesh_scoping(self) -> Union[core.Scoping, core.outputs.Output, None]:
        """Generate a mesh_scoping from input arguments."""
        pass

    def _build_result_operator(
        self,
        name: str,
        time_scoping: core.Scoping,
        mesh_scoping: Union[core.Scoping, core.outputs.Output],
        location: core.locations,
    ) -> core.Operator:
        op = self._model.operator(name=name)
        # Set the time_scoping if necessary
        if time_scoping:
            op.connect(0, time_scoping)
        # Set the mesh_scoping if necessary
        if mesh_scoping:
            op.connect(1, mesh_scoping)

        op.connect(7, self.mesh._meshed_region)
        op.connect(9, location)
        return op


class MechanicalSimulation(Simulation, ABC):
    """Base class for mechanical type simulations.

    This class provides common methods and properties for all mechanical type simulations.
    """

    def __init__(self, data_sources: core.DataSources, model: core.Model):
        """Instantiate a mechanical type simulation."""
        super().__init__(data_sources, model)

    def _build_mesh_scoping(
        self,
        selection=None,
        named_selections=None,
        element_ids=None,
        node_ids=None,
        location=core.locations.nodal,
    ) -> Union[core.Scoping, core.outputs.Output, None]:
        """Generate a mesh_scoping from input arguments.

        Only one input is used, by order of priority: selection, named_selection,
        element_ids, node_ids.

        Args:
            selection:
                Selection object to use.
            named_selections:
                Named selection to use.
            element_ids:
                Element IDs to use.
            node_ids:
                Node IDs to use.
            location:
                Requested location for the returned Scoping.

        Returns
        -------
            Returns a mesh Scoping or an operator Output giving a mesh Scoping.
        """
        tot = (
            (node_ids is not None)
            + (element_ids is not None)
            + (named_selections is not None)
            + (selection is not None)
        )
        if tot > 1:
            raise ValueError(
                "Arguments selection, named_selections, element_ids, "
                "and node_ids are mutually exclusive"
            )

        # Build the mesh_scoping
        mesh_scoping = None
        if selection:
            mesh_scoping = selection.mesh_scoping_output

        if named_selections:
            if type(named_selections) == str:
                mesh_scoping_op = self._model.operator("scoping_provider_by_ns")
                mesh_scoping_op.connect(1, named_selections)
                mesh_scoping = mesh_scoping_op.outputs.mesh_scoping
            elif type(named_selections) == list:
                merge_scopings_op = self._model.operator(name="merge::scoping")
                for pin, named_selection in enumerate(named_selections):
                    mesh_scoping_on_ns_op = self._model.operator(
                        name="scoping_provider_by_ns"
                    )
                    mesh_scoping_on_ns_op.connect(0, location)
                    mesh_scoping_on_ns_op.connect(1, named_selection)
                    merge_scopings_op.connect(
                        pin, mesh_scoping_on_ns_op.outputs.mesh_scoping
                    )
                mesh_scoping = merge_scopings_op.outputs.merged_scoping

        elif element_ids:
            mesh_scoping = core.mesh_scoping_factory.elemental_scoping(
                element_ids=element_ids, server=self._model._server
            )
            # Transpose location if necessary
            if location == core.locations.nodal:
                transpose_op = self._model.operator(name="transpose_scoping")
                transpose_op.connect(0, mesh_scoping)
                transpose_op.connect(1, self.mesh._meshed_region)
                transpose_op.connect(2, 0)
                mesh_scoping = transpose_op.outputs.mesh_scoping_as_scoping

        elif node_ids:
            mesh_scoping = core.mesh_scoping_factory.nodal_scoping(
                node_ids, server=self._model._server
            )

        return mesh_scoping

    def _build_time_freq_scoping(
        self,
        selection: Union[Selection, None],
        set_ids: Union[int, List[int], None],
        times: Union[float, List[float], None],
        load_steps: Union[
            int, List[int], Tuple[int, Union[int, List[int]]], None
        ] = None,
        all_sets: bool = False,
    ) -> core.time_freq_scoping_factory.Scoping:
        """Generate a time_freq_scoping from input arguments.

        Only one input is used, by order of priority:
        all_sets, selection, set_ids, times, load_steps.

        Args:
            selection:
                Selection to use (used in priority).
            set_ids:
                List of set IDs to use, if no selection is defined.
            times:
                Time values to use, if no selection nor set_ids are defined.
            load_steps:
                Load step IDs (and sub-step if tuple) to use, if no other is defined.
            all_sets:
                Whether to force extraction of all sets.

        Returns
        -------
            A Scoping corresponding to the requested input, with time location.
        """
        tot = (
            (set_ids is not None)
            + (all_sets is True)
            + (times is not None)
            + (load_steps is not None)
            + (selection is not None)
        )
        if tot > 1:
            raise ValueError(
                "Arguments all_sets, selection, set_ids, times, "
                "and load_steps are mutually exclusive."
            )
        if all_sets:
            return core.time_freq_scoping_factory.scoping_on_all_time_freqs(self._model)
        # create from selection
        if selection:
            return selection.time_freq_selection._evaluate_on(simulation=self)
        # else from set_ids
        if set_ids is not None:
            if isinstance(set_ids, int):
                set_ids = [set_ids]
            return core.time_freq_scoping_factory.scoping_by_sets(
                cumulative_sets=set_ids, server=self._model._server
            )
        # else from times
        if times is not None:
            # Check input
            if isinstance(times, list):
                if any([not (type(t) in [float, int]) for t in times]):
                    raise ValueError("Argument times must contain numeric values only.")
            elif isinstance(times, float) or isinstance(times, int):
                times = [times]
            else:
                raise TypeError("Argument times must be a number or a list of numbers.")

            # Get the set_ids for available time values matching the requested time values.
            available_times = self.time_freq_support.time_frequencies.data
            precision = self._get_time_freq_precision
            available_times_to_extract_set_ids = []
            last_extracted_index = -1
            len_available = len(available_times)
            for t in times:
                found = False
                i = last_extracted_index + 1
                while not found and i < len_available:
                    if abs(float(t) - available_times[i]) < precision:
                        last_extracted_index = i
                        available_times_to_extract_set_ids.append(i + 1)
                        found = True
                    i += 1
                if not found:
                    raise ValueError(
                        f"Could not find time={t}{self.units['time/frequency']} "
                        f"in the simulation."
                    )
            return core.time_freq_scoping_factory.scoping_by_sets(
                cumulative_sets=available_times_to_extract_set_ids,
                server=self._model._server,
            )

        # else from load_steps
        if load_steps is not None:
            # If load_steps and sub_steps
            if len(load_steps) == 2:
                # Translate to cumulative indices (set IDs)
                set_ids = []
                sub_steps = load_steps[1]
                if not isinstance(sub_steps, list):
                    sub_steps = [sub_steps]
                set_id_0 = (
                    self._model.metadata.time_freq_support.get_cumulative_index(
                        step=load_steps[0] - 1, substep=sub_steps[0]
                    )
                    + 2
                )
                set_ids.extend([set_id_0 + i for i in range(len(sub_steps))])
                return core.time_freq_scoping_factory.scoping_by_sets(
                    cumulative_sets=set_ids, server=self._model._server
                )
            if isinstance(load_steps, int):
                load_steps = [load_steps]
            return core.time_freq_scoping_factory.scoping_by_load_steps(
                load_steps=load_steps, server=self._model._server
            )
        # Otherwise, no argument was given, create a time_freq_scoping of the last set only
        return core.time_freq_scoping_factory.scoping_by_set(
            cumulative_set=self.time_freq_support.n_sets, server=self._model._server
        )


class ModalMechanicalSimulation(MechanicalSimulation):
    """Provides methods for mechanical modal simulations."""

    def _build_time_freq_scoping(self) -> core.time_freq_scoping_factory.Scoping:
        """Generate a time_freq_scoping from input arguments."""
        pass


class HarmonicMechanicalSimulation(MechanicalSimulation):
    """Provides methods for mechanical harmonic simulations."""

    def _build_time_freq_scoping(self) -> core.time_freq_scoping_factory.Scoping:
        """Generate a time_freq_scoping from input arguments."""
        pass