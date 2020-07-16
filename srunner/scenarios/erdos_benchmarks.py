import py_trees
import random
import carla

from srunner.scenariomanager.carla_data_provider import CarlaDataProvider
from srunner.scenariomanager.scenarioatomics.atomic_behaviors import \
    ActorDestroy, ActorTransformSetter, ActorRotationSetter, KeepVelocity
from srunner.scenariomanager.scenarioatomics.atomic_criteria import \
    CollisionTest, MaxSimTimeTest
from srunner.scenariomanager.scenarioatomics.atomic_trigger_conditions import \
    DriveDistance, InTriggerDistanceToLocation, InTriggerDistanceToVehicle, \
    InTriggerRegion, StandStill
from srunner.scenarios.basic_scenario import BasicScenario

LEFT_PEDESTRIAN_LOCATIONS = [
    carla.Location(x=78.412392, y=323.170654, z=0.178421),
    carla.Location(x=68.418488, y=322.162109, z=0.178421),
    carla.Location(x=242.724152, y=317.176208, z=0.178421),
    carla.Location(x=153.504883, y=323.505646, z=0.178421),
    carla.Location(x=96.705582, y=314.969849, z=0.178421),
    carla.Location(x=97.432373, y=322.244598, z=0.178421),
    carla.Location(x=281.080444, y=319.154968, z=0.178421),
    carla.Location(x=47.836460, y=321.374847, z=0.178421),
    carla.Location(x=258.185059, y=318.115021, z=0.178421),
    carla.Location(x=251.518860, y=323.782043, z=0.178421),
    carla.Location(x=159.216705, y=323.816833, z=0.178421),
    carla.Location(x=187.085022, y=319.443115, z=0.127962),
    carla.Location(x=33.870499, y=322.020935, z=0.178421),
    carla.Location(x=167.093018, y=323.526306, z=0.178421),
    carla.Location(x=289.059448, y=323.221558, z=0.178421),
    carla.Location(x=223.962784, y=322.296570, z=0.178421),
    carla.Location(x=59.481533, y=322.036041, z=0.178421),
    carla.Location(x=251.175629, y=314.260284, z=0.178421),
    carla.Location(x=299.531342, y=316.869080, z=0.178421),
    carla.Location(x=322.869507, y=318.211365, z=0.178421),
    carla.Location(x=321.886169, y=317.148987, z=0.178421),
    carla.Location(x=265.808594, y=319.808716, z=0.178421),
    carla.Location(x=367.223083, y=322.735931, z=0.178421),
    carla.Location(x=68.458603, y=323.804840, z=0.178421),
    carla.Location(x=85.879257, y=318.511047, z=0.178421),
    carla.Location(x=237.172943, y=321.682190, z=0.178421),
    carla.Location(x=325.161774, y=313.713806, z=0.178421),
    carla.Location(x=29.981731, y=322.035217, z=0.178421),
    carla.Location(x=218.551392, y=323.960327, z=0.178421),
    carla.Location(x=389.259979, y=315.975922, z=0.178421),
    carla.Location(x=51.546616, y=324.047668, z=0.178421),
    carla.Location(x=95.118416, y=314.533630, z=0.178421),
    carla.Location(x=304.154114, y=318.742523, z=0.178421),
    carla.Location(x=293.317535, y=316.227295, z=0.178421),
    carla.Location(x=128.972229, y=322.892853, z=0.178421),
    carla.Location(x=249.703064, y=313.867462, z=0.178421),
    carla.Location(x=322.273193, y=322.278992, z=0.178421),
    carla.Location(x=272.732605, y=320.105988, z=0.178421),
    carla.Location(x=14.837142, y=321.624939, z=0.178421),
    carla.Location(x=190.210724, y=321.813049, z=0.178421),
    carla.Location(x=184.097626, y=323.372925, z=0.178421),
    carla.Location(x=175.718842, y=321.901978, z=0.178421),
    carla.Location(x=304.629486, y=317.572845, z=0.178421),
    carla.Location(x=316.855194, y=319.423187, z=0.178421),
    carla.Location(x=33.428959, y=322.850220, z=0.178421),
    carla.Location(x=128.266373, y=323.771790, z=0.178421),
    carla.Location(x=342.038818, y=318.311249, z=0.178421),
    carla.Location(x=31.766727, y=322.702301, z=0.178421),
    carla.Location(x=299.167053, y=323.124878, z=0.178421),
    carla.Location(x=140.243896, y=322.242981, z=0.178421),
    carla.Location(x=276.190491, y=321.081635, z=0.178421),
    carla.Location(x=14.218060, y=321.422974, z=0.178421),
    carla.Location(x=37.528347, y=323.550293, z=0.178421),
    carla.Location(x=239.099762, y=322.389954, z=0.178421),
    carla.Location(x=275.256287, y=316.526398, z=0.178421),
]

RIGHT_PEDESTRIAN_LOCATIONS = [
    carla.Location(x=350.550201, y=335.187317, z=0.178421),
    carla.Location(x=232.981644, y=334.388306, z=0.178421),
    carla.Location(x=188.743835, y=333.404907, z=0.178421),
    carla.Location(x=164.170914, y=335.196686, z=0.178421),
    carla.Location(x=15.209345, y=335.201416, z=0.178421),
    carla.Location(x=359.794922, y=334.626587, z=0.178421),
    carla.Location(x=266.455139, y=334.497192, z=0.178421),
    carla.Location(x=114.930313, y=334.799988, z=0.178421),
    carla.Location(x=50.893738, y=333.211700, z=0.178421),
    carla.Location(x=171.739258, y=334.297699, z=0.178421),
    carla.Location(x=47.960590, y=335.595856, z=0.178421),
    carla.Location(x=207.187683, y=333.949402, z=0.178421),
    carla.Location(x=80.272377, y=333.790161, z=0.178421),
    carla.Location(x=384.441345, y=335.221680, z=0.178421),
    carla.Location(x=122.811996, y=333.855499, z=0.178421),
    carla.Location(x=344.781494, y=333.570801, z=0.178421),
    carla.Location(x=173.823975, y=334.220032, z=0.178421),
    carla.Location(x=144.417786, y=335.413452, z=0.178421),
    carla.Location(x=383.538208, y=335.320740, z=0.178421),
    carla.Location(x=389.220886, y=334.166260, z=0.178421),
    carla.Location(x=223.445312, y=334.052704, z=0.178421),
    carla.Location(x=76.547646, y=335.064697, z=0.178421),
    carla.Location(x=220.296692, y=334.691833, z=0.178421),
    carla.Location(x=280.560150, y=335.657440, z=0.178421),
    carla.Location(x=257.465332, y=333.976318, z=0.178421),
    carla.Location(x=332.581879, y=333.940979, z=0.178421),
    carla.Location(x=147.433990, y=334.056854, z=0.178421),
    carla.Location(x=355.586273, y=334.151154, z=0.178421),
    carla.Location(x=348.346313, y=334.907135, z=0.178421),
    carla.Location(x=218.856461, y=334.872314, z=0.178421),
    carla.Location(x=91.295258, y=334.089172, z=0.178421),
    carla.Location(x=220.347900, y=335.830750, z=0.178421),
    carla.Location(x=98.719185, y=335.502411, z=0.178421),
    carla.Location(x=19.872103, y=333.940002, z=0.178421),
    carla.Location(x=222.739853, y=335.307434, z=0.178421),
    carla.Location(x=366.510742, y=335.127716, z=0.178421),
]


class ERDOSPedestrianBehindCar(BasicScenario):
    """
    This class sets up the scenario where the ego vehicle needs to drive
    on a road, and a pedestrian crosses unexpectedly from the other side of
    the road.

    This is a single ego vehicle scenario
    """
    def __init__(self,
                 world,
                 ego_vehicles,
                 config,
                 randomize=False,
                 debug_mode=False,
                 criteria_enable=True,
                 timeout=600000000000,
                 coca_cola_van_distance=110,
                 coca_cola_van_translation=4,
                 pedestrian_distance=117,
                 pedestrian_translation=4.5,
                 pedestrian_velocity=2.75,
                 pedestrian_trigger_distance=26,
                 pedestrian_yaw_offset=90,
                 crossing_distance=4.5,
                 pedestrian_bp_name='walker.pedestrian.0008',
                 truck_bp_name='vehicle.carlamotors.carlacola',
                 rotate_pedestrian=True):
        """
        Sets up the required class variables and calls BasicScenario to
        finish setting up the scenario.
        """
        self.debug_mode = debug_mode
        self._map = CarlaDataProvider.get_map()
        self._world = CarlaDataProvider.get_world()
        self._reference_waypoint = self._map.get_waypoint(
            config.trigger_points[0].location)
        self.timeout = timeout

        # Coca Cola Van Config
        self._coca_cola_van_distance = coca_cola_van_distance
        self._coca_cola_van_translation = coca_cola_van_translation
        self._truck_bp_name = truck_bp_name

        # Pedestrian Config
        self._pedestrian_distance = pedestrian_distance
        self._pedestrian_translation = pedestrian_translation
        self._pedestrian_velocity = pedestrian_velocity
        self._pedestrian_trigger_distance = pedestrian_trigger_distance
        self._pedestrian_yaw_offset = pedestrian_yaw_offset
        self._pedestrian_bp_name = pedestrian_bp_name
        self._rotate_pedestrian = rotate_pedestrian

        # Miscellaneous Config
        self._crossing_distance = crossing_distance
        self._driving_distance = 180

        # Call the base class to set up the scenario.
        super(ERDOSPedestrianBehindCar,
              self).__init__("ERDOSPedestrianBehindCar",
                             ego_vehicles,
                             config,
                             world,
                             debug_mode,
                             criteria_enable=criteria_enable)

    @staticmethod
    def get_waypoint_in_distance(waypoint, distance):
        """
        Obtain a waypoint in a given distance from the actor's location.
        Do not stop the search on the first intersection.
        """
        traveled_distance = 0
        while traveled_distance < distance:
            waypoint_new = waypoint.next(1.0)[0]
            traveled_distance += waypoint_new.transform.location.distance(
                waypoint.transform.location)
            waypoint = waypoint_new

        return waypoint, traveled_distance

    def _initialize_actors(self, config):
        """
        Initializes the other vehicles in the scenario.
        """
        # Initialize the coca cola truck.
        coca_cola_van_wp, _ = ERDOSPedestrianBehindCar.get_waypoint_in_distance(
            self._reference_waypoint, self._coca_cola_van_distance)
        self._coca_cola_van_transform = carla.Transform(
            carla.Location(
                coca_cola_van_wp.transform.location.x,
                coca_cola_van_wp.transform.location.y +
                self._coca_cola_van_translation,
                coca_cola_van_wp.transform.location.z + 1),
            carla.Rotation(coca_cola_van_wp.transform.rotation.pitch,
                           coca_cola_van_wp.transform.rotation.yaw + 180,
                           coca_cola_van_wp.transform.rotation.roll))
        coca_cola_van = CarlaDataProvider.request_new_actor(
            self._truck_bp_name, self._coca_cola_van_transform, color='red')
        self.other_actors.append(coca_cola_van)

        # Initialize the pedestrian.
        pedestrian_wp, _ = ERDOSPedestrianBehindCar.get_waypoint_in_distance(
            self._reference_waypoint, self._pedestrian_distance)
        self._pedestrian_transform = carla.Transform(
            carla.Location(
                pedestrian_wp.transform.location.x,
                pedestrian_wp.transform.location.y +
                self._pedestrian_translation,
                pedestrian_wp.transform.location.z + 5),
            carla.Rotation(
                pedestrian_wp.transform.rotation.pitch,
                pedestrian_wp.transform.rotation.yaw +
                self._pedestrian_yaw_offset,
                pedestrian_wp.transform.rotation.roll))
        pedestrian = CarlaDataProvider.request_new_actor(
            self._pedestrian_bp_name,
            self._pedestrian_transform,
            color='red',
            rolename='pedestrian')
        self.other_actors.append(pedestrian)

        # Set all the traffic lights in the world to green.
        for actor in self._world.get_actors():
            if actor.type_id == "traffic.traffic_light":
                actor.set_state(carla.TrafficLightState.Green)
                actor.freeze(True)

    def _create_behavior(self):
        """
        The scenario involves setting up a set of vehicles, and having a
        pedestrian run from in between the vehicles in front of the ego
        vehicle.
        """

        # First, fix the transform of the other actors in the scene.
        coca_cola_transform = ActorTransformSetter(
            self.other_actors[0], self._coca_cola_van_transform)

        # The pedestrian needs to walk to the other side of the road.
        pedestrian_crossing = py_trees.composites.Parallel(
            "Obstacle clearing road",
            policy=py_trees.common.ParallelPolicy.SUCCESS_ON_ONE)
        pedestrian_crossing.add_child(
            DriveDistance(self.other_actors[-1], self._crossing_distance))
        pedestrian_crossing.add_child(
            KeepVelocity(self.other_actors[-1],
                         self._pedestrian_velocity,
                         distance=self._crossing_distance))

        # The pedestrian needs to face us to make detection easier.
        pedestrian_rotation = ActorRotationSetter(self.other_actors[-1], 90)

        # Define the endcondition.
        endcondition = py_trees.composites.Parallel(
            "Waiting for end position",
            policy=py_trees.common.ParallelPolicy.SUCCESS_ON_ALL)
        reached_goal = InTriggerDistanceToLocation(
            self.ego_vehicles[0], self._reference_waypoint.transform.location -
            carla.Location(x=self._driving_distance), 5)
        endcondition.add_child(reached_goal)

        # Define the behavior tree.
        sequence = py_trees.composites.Sequence(
            "PedestrianBehindCar Behavior Tree")
        sequence.add_child(coca_cola_transform)
        sequence.add_child(
            InTriggerDistanceToVehicle(self.other_actors[-1],
                                       self.ego_vehicles[0],
                                       self._pedestrian_trigger_distance))
        sequence.add_child(pedestrian_crossing)
        if self._rotate_pedestrian:
            sequence.add_child(pedestrian_rotation)
        sequence.add_child(endcondition)
        sequence.add_child(ActorDestroy(self.other_actors[0]))
        sequence.add_child(ActorDestroy(self.other_actors[-1]))

        return sequence

    def _create_test_criteria(self):
        """
        A list of all test criteria will be created that is later used
        in parallel behavior tree.
        """
        criteria = []
        collision_criterion = CollisionTest(self.ego_vehicles[0],
                                            terminate_on_failure=True,
                                            num_updates_after_failure=10)
        criteria.append(collision_criterion)
        # Do no add the simulation time constraint when running in debug mode.
        if not self.debug_mode:
            # The scenario should run for 50 simulation time seconds.
            timely_arrival = MaxSimTimeTest(self.ego_vehicles[0],
                                            30,
                                            terminate_on_failure=True)
            criteria.append(timely_arrival)
        return criteria

    def __del__(self):
        """
        Remove all actors upon deletion
        """
        self.remove_all_actors()


class ERDOSPedestrianBehindParkedCar(ERDOSPedestrianBehindCar):
    def __init__(self,
                 world,
                 ego_vehicles,
                 config,
                 randomize=False,
                 debug_mode=False,
                 criteria_enable=True,
                 timeout=600000000000):
        super(ERDOSPedestrianBehindParkedCar,
              self).__init__(world,
                             ego_vehicles,
                             config,
                             randomize,
                             debug_mode,
                             criteria_enable,
                             timeout,
                             62,
                             -3.5,
                             65,
                             -3.25,
                             2.5,
                             25,
                             -90,
                             2.5,
                             truck_bp_name='vehicle.volkswagen.t2')


class ERDOSCarBehindTruck(ERDOSPedestrianBehindCar):
    def __init__(self,
                 world,
                 ego_vehicles,
                 config,
                 randomize=False,
                 debug_mode=False,
                 criteria_enable=True,
                 timeout=600000000000):
        super(ERDOSCarBehindTruck,
              self).__init__(world,
                             ego_vehicles,
                             config,
                             randomize,
                             debug_mode,
                             criteria_enable,
                             timeout,
                             88,
                             4,
                             100,
                             4.5,
                             7.5,
                             45,
                             90,
                             3.0,
                             pedestrian_bp_name='vehicle.nissan.micra',
                             rotate_pedestrian=False)


class ERDOSManyPedestrians(BasicScenario):
    """
    This class sets up the scenario with a large number of actors in the
    field of vision so as to increase the runtime of the object detectors
    and force a change in the optimum configuration.

    This is a single ego-vehicle scenario.
    """
    def __init__(self,
                 world,
                 ego_vehicles,
                 config,
                 randomize=False,
                 debug_mode=False,
                 criteria_enable=True,
                 timeout=600000000000):
        """
        Sets up the required class variables and calls BasicScenario to
        finish setting up the scenario.
        """
        self.debug_mode = debug_mode
        self._map = CarlaDataProvider.get_map()
        self._world = CarlaDataProvider.get_world()
        self._reference_waypoint = self._map.get_waypoint(
            config.trigger_points[0].location)
        self.timeout = timeout

        # Number of pedestrians in the scene.
        self._num_walkers = 91
        # Pedestrian Config.
        self._pedestrian_distance = 132
        self._pedestrian_trigger_distance = 50
        self._pedestrian_translation = 6
        self._pedestrian_velocity = 6

        # Miscellaneous Config
        self._crossing_distance = 10
        self._driving_distance = 370

        # Call the base class to set up the scenario.
        super(ERDOSManyPedestrians,
              self).__init__("ERDOSManyPedestrians",
                             ego_vehicles,
                             config,
                             world,
                             debug_mode,
                             criteria_enable=criteria_enable)

    def spawn_pedestrians(self, sampled_locations, goto_locations):
        """
        Spawns the pedestrians at the sampled locations and makes them
        complete a trajectory to the corresponding location in the goto
        locations.

        Returns the actors spawned.
        """
        actors = []
        for location, destination in zip(sampled_locations, goto_locations):
            # Spawn the actor.
            walker_bp = random.choice(
                self._world.get_blueprint_library().filter("walker.*"))
            try:
                walker_actor = self._world.spawn_actor(
                    walker_bp, carla.Transform(location=location))
            except RuntimeError:
                print("Could not spawn the actor because of collision.")
                continue
            actors.append(walker_actor)

            # Spawn the controller.
            walker_controller_bp = self._world.get_blueprint_library().find(
                'controller.ai.walker')
            walker_controller_actor = self._world.spawn_actor(
                walker_controller_bp, carla.Transform(), walker_actor)

            self._world.wait_for_tick()

            # Choose a location and make the pedestrian move there.
            walker_controller_actor.start()
            walker_controller_actor.go_to_location(destination)
            walker_controller_actor.set_max_speed(1.4)

        return actors

    def _initialize_actors(self, config):
        """
        Initializes the other vehicles in the scenario.
        """
        # Initialize all the pedestrians in the scene.
        if self._num_walkers > len(LEFT_PEDESTRIAN_LOCATIONS) + len(
                RIGHT_PEDESTRIAN_LOCATIONS):
            raise ValueError(
                "The number of walkers requested ({}) is greater than the "
                "number of unique pedestrian locations ({}).".format(
                    self._num_walkers,
                    len(LEFT_PEDESTRIAN_LOCATIONS) +
                    len(RIGHT_PEDESTRIAN_LOCATIONS)))

        left_locations, right_locations = [], []
        # To ensure that there is determinism across runs, and still be able
        # to use random.sample
        random.seed(0)
        if self._num_walkers // 2 >= len(RIGHT_PEDESTRIAN_LOCATIONS):
            right_locations = RIGHT_PEDESTRIAN_LOCATIONS
            left_locations = random.sample(
                LEFT_PEDESTRIAN_LOCATIONS,
                self._num_walkers - len(RIGHT_PEDESTRIAN_LOCATIONS))
        else:
            right_locations = random.sample(RIGHT_PEDESTRIAN_LOCATIONS,
                                            self._num_walkers // 2)
            left_locations = random.sample(
                LEFT_PEDESTRIAN_LOCATIONS,
                self._num_walkers - (self._num_walkers // 2))

        # Spawn the pedestrians on the left and right hand sides of the road.
        self.other_actors.extend(
            self.spawn_pedestrians(
                right_locations,
                random.sample(RIGHT_PEDESTRIAN_LOCATIONS,
                              len(right_locations))))
        self.other_actors.extend(
            self.spawn_pedestrians(
                left_locations,
                random.sample(LEFT_PEDESTRIAN_LOCATIONS, len(left_locations))))

        # Set all the traffic lights in the world to green.
        for actor in self._world.get_actors():
            if actor.type_id == "traffic.traffic_light":
                actor.set_state(carla.TrafficLightState.Green)
                actor.freeze(True)

    def _create_behavior(self):
        """
        The scenario involves setting up a set of vehicles, and having a
        pedestrian run from in between the vehicles in front of the ego
        vehicle.
        """
        # Define the endcondition.
        endcondition = py_trees.composites.Parallel(
            "Waiting for end position",
            policy=py_trees.common.ParallelPolicy.SUCCESS_ON_ALL)
        reached_goal = InTriggerDistanceToLocation(
            self.ego_vehicles[0], self._reference_waypoint.transform.location -
            carla.Location(x=self._driving_distance), 5)
        endcondition.add_child(reached_goal)

        # Define the behavior tree.
        sequence = py_trees.composites.Sequence(
            "ManyPedestrians Behavior Tree")
        sequence.add_child(endcondition)
        for actor in self.other_actors:
            sequence.add_child(ActorDestroy(actor))

        return sequence

    def _create_test_criteria(self):
        """
        A list of all test criteria will be created that is later used
        in parallel behavior tree.
        """
        criteria = []
        collision_criterion = CollisionTest(self.ego_vehicles[0],
                                            terminate_on_failure=True,
                                            num_updates_after_failure=10)
        criteria.append(collision_criterion)
        # Do no add the simulation time constraint when running in debug mode.
        if not self.debug_mode:
            # The scenario should run for 50 simulation time seconds.
            timely_arrival = MaxSimTimeTest(self.ego_vehicles[0],
                                            50,
                                            terminate_on_failure=True)
            criteria.append(timely_arrival)
        return criteria

    def __del__(self):
        """
        Remove all actors upon deletion
        """
        self.remove_all_actors()


class ERDOSCarRunningLight(BasicScenario):
    """
    This class sets up the scenario where the ego vehicle needs to drive
    on a road, and a car runs a traffic light from the left hand side.
    """
    def __init__(self,
                 world,
                 ego_vehicles,
                 config,
                 randomize=False,
                 debug_mode=False,
                 criteria_enable=True,
                 timeout=600000000000):
        self.debug_mode = debug_mode
        self._map = CarlaDataProvider.get_map()
        self._world = CarlaDataProvider.get_world()
        self._reference_waypoint = self._map.get_waypoint(
            config.trigger_points[0].location)
        self.timeout = timeout

        # Other vehicle config.
        self._vehicle_distance = 323
        self._crossing_distance = 40
        self._vehicle_velocity = 10
        self._vehicle_translation = 50
        self._vehicle_trigger_distance = 150

        # Ego vehicle config
        self._driving_distance = 370

        # Call the base class to set up the scenario.
        super(ERDOSCarRunningLight,
              self).__init__("ERDOSCarRunningLight",
                             ego_vehicles,
                             config,
                             world,
                             debug_mode,
                             criteria_enable=criteria_enable)

    @staticmethod
    def get_waypoint_in_distance(waypoint, distance):
        """
        Obtain a waypoint in a given distance from the actor's location.
        Do not stop the search on the first intersection.
        """
        traveled_distance = 0
        while traveled_distance < distance:
            waypoint_new = waypoint.next(1.0)[0]
            traveled_distance += waypoint_new.transform.location.distance(
                waypoint.transform.location)
            waypoint = waypoint_new

        return waypoint, traveled_distance

    def _initialize_actors(self, config):
        """
        Initializes the other vehicles in the scenario.
        """
        # Initialize the other vehicle.
        vehicle_wp, _ = ERDOSCarRunningLight.get_waypoint_in_distance(
            self._reference_waypoint, self._vehicle_distance)
        self._vehicle_transform = carla.Transform(
            carla.Location(
                vehicle_wp.transform.location.x,
                vehicle_wp.transform.location.y - self._vehicle_translation,
                vehicle_wp.transform.location.z + 10),
            carla.Rotation(vehicle_wp.transform.rotation.pitch, 90,
                           vehicle_wp.transform.rotation.roll))
        vehicle = CarlaDataProvider.request_new_actor('vehicle.audi.a2',
                                                   self._vehicle_transform,
                                                   rolename='vehicle')
        self.other_actors.append(vehicle)

        # Set all the traffic lights in the world to green.
        for actor in self._world.get_actors():
            if actor.type_id == "traffic.traffic_light":
                actor.set_state(carla.TrafficLightState.Green)
                actor.freeze(True)

    def _create_behavior(self):
        """
        The scenario involves setting up a set of vehicles, and having a
        pedestrian run from in between the vehicles in front of the ego
        vehicle.
        """
        # The vehicle needs to drive to the other side.
        vehicle_crossing = py_trees.composites.Parallel(
            "Obstacle clearing road",
            policy=py_trees.common.ParallelPolicy.SUCCESS_ON_ONE)
        vehicle_crossing.add_child(
            DriveDistance(self.other_actors[0], self._crossing_distance))
        vehicle_crossing.add_child(
            KeepVelocity(self.other_actors[0], self._vehicle_velocity))

        # Define the endcondition.
        endcondition = py_trees.composites.Parallel(
            "Waiting for end position",
            policy=py_trees.common.ParallelPolicy.SUCCESS_ON_ALL)
        reached_goal = InTriggerDistanceToLocation(
            self.ego_vehicles[0], self._reference_waypoint.transform.location +
            carla.Location(x=self._driving_distance), 5)
        endcondition.add_child(reached_goal)

        # Define the behavior tree.
        sequence = py_trees.composites.Sequence(
            "ERDOSCarRunningLight Behavior Tree")
        sequence.add_child(
            InTriggerDistanceToVehicle(self.other_actors[0],
                                       self.ego_vehicles[0],
                                       self._vehicle_trigger_distance))
        sequence.add_child(vehicle_crossing)
        sequence.add_child(
            InTriggerDistanceToLocation(
                self.ego_vehicles[0],
                self._reference_waypoint.transform.location +
                carla.Location(x=self._driving_distance), 100))
        sequence.add_child(endcondition)
        sequence.add_child(ActorDestroy(self.other_actors[0]))

        return sequence

    def _create_test_criteria(self):
        """
        A list of all test criteria will be created that is later used
        in parallel behavior tree.
        """
        criteria = []
        collision_criterion = CollisionTest(self.ego_vehicles[0],
                                            terminate_on_failure=True,
                                            num_updates_after_failure=10)
        criteria.append(collision_criterion)
        # Do no add the simulation time constraint when running in debug mode.
        if not self.debug_mode:
            # The scenario should run for 50 simulation time seconds.
            timely_arrival = MaxSimTimeTest(self.ego_vehicles[0],
                                            50,
                                            terminate_on_failure=True)
            criteria.append(timely_arrival)
        return criteria

    def __del__(self):
        """
        Remove all actors upon deletion
        """
        self.remove_all_actors()


class ERDOSCarFromAlley(BasicScenario):
    def __init__(self,
                 world,
                 ego_vehicles,
                 config,
                 randomize=False,
                 debug_mode=False,
                 criteria_enable=True,
                 timeout=600000000000):
        self.debug_mode = debug_mode
        self._map = CarlaDataProvider.get_map()
        self._world = CarlaDataProvider.get_world()
        self._reference_waypoint = self._map.get_waypoint(
            config.trigger_points[0].location)
        self.timeout = timeout

        # Other vehicle config.
        self._crossing_distance = 1.75
        self._vehicle_velocity = 2.5
        self._vehicle_trigger_distance = 60

        self._driving_distance = 250

        # Call the base class to set up the scenario.
        super(ERDOSCarFromAlley,
              self).__init__("ERDOSCarFromAlley",
                             ego_vehicles,
                             config,
                             world,
                             debug_mode,
                             criteria_enable=criteria_enable)

    def _initialize_actors(self, config):
        """
        Initializes the other vehicles in the scenario.
        """
        alley_transform = carla.Transform(carla.Location(80.7, 285.7, 2),
                                          carla.Rotation(0, 0, 0))
        alley_tesla = CarlaDataProvider.request_new_actor('vehicle.tesla.model3',
                                                       alley_transform)
        self.other_actors.append(alley_tesla)
        # Set all the traffic lights in the world to green.
        for actor in self._world.get_actors():
            if actor.type_id == "traffic.traffic_light":
                actor.set_state(carla.TrafficLightState.Green)
                actor.freeze(True)

    def _create_behavior(self):
        # The vehicle needs to drive to the other side.
        vehicle_crossing = py_trees.composites.Parallel(
            "Obstacle clearing road",
            policy=py_trees.common.ParallelPolicy.SUCCESS_ON_ONE)
        vehicle_crossing.add_child(
            KeepVelocity(self.other_actors[0],
                         self._vehicle_velocity,
                         distance=self._crossing_distance))

        # Define the end condition.
        endcondition = py_trees.composites.Parallel(
            "Waiting for end position",
            policy=py_trees.common.ParallelPolicy.SUCCESS_ON_ALL)
        reached_goal = InTriggerDistanceToLocation(
            self.ego_vehicles[0], self._reference_waypoint.transform.location +
            carla.Location(y=self._driving_distance), 5)
        endcondition.add_child(reached_goal)

        # Define the behavior tree.
        sequence = py_trees.composites.Sequence("CarFromAlley Behavior Tree")
        sequence.add_child(
            InTriggerDistanceToVehicle(self.other_actors[0],
                                       self.ego_vehicles[0],
                                       self._vehicle_trigger_distance))
        sequence.add_child(vehicle_crossing)
        sequence.add_child(endcondition)
        sequence.add_child(ActorDestroy(self.other_actors[0]))

        return sequence

    def _create_test_criteria(self):
        """
        A list of all test criteria will be created that is later used
        in parallel behavior tree.
        """
        criteria = []
        collision_criterion = CollisionTest(self.ego_vehicles[0],
                                            terminate_on_failure=True,
                                            num_updates_after_failure=10)
        criteria.append(collision_criterion)

        # Do not add the simulation time criteria when running in debug mode.
        if not self.debug_mode:
            timely_arrival = MaxSimTimeTest(self.ego_vehicles[0],
                                            50,
                                            terminate_on_failure=True)
            criteria.append(timely_arrival)

        return criteria

    def __del__(self):
        """
        Remove all actors upon deletion
        """
        self.remove_all_actors()


class ERDOSTrackPedestrians(BasicScenario):
    """
    This class sets up the scenario with 5-10 actors in the field of
    vision. This simple scenario is used to evaluate pedestrian
    tracking.

    This is a single ego-vehicle scenario.
    """
    def __init__(self,
                 world,
                 ego_vehicles,
                 config,
                 randomize=False,
                 debug_mode=False,
                 criteria_enable=True,
                 timeout=600000000000):
        """
        Sets up the required class variables and calls BasicScenario to
        set up most of the scenario.
        """
        self.debug_mode = debug_mode
        self._map = CarlaDataProvider.get_map()
        self._world = CarlaDataProvider.get_world()
        self._reference_waypoint = self._map.get_waypoint(
            config.trigger_points[0].location)
        self.timeout = timeout

        # Number of pedestrians in the scene
        self._num_walkers = 12

        # Pedestrian Config.
        self._pedestrian_distance = 132
        self._pedestrian_trigger_distance = 50
        self._pedestrian_translation = 6
        self._pedestrian_velocity = 6

        self._driving_distance = 370
        # Call the base class to set up the scenario.
        super(ERDOSTrackPedestrians,
              self).__init__("ERDOSTrackPedestrians",
                             ego_vehicles,
                             config,
                             world,
                             debug_mode,
                             criteria_enable=criteria_enable)

    def spawn_pedestrians(self, sampled_locations, goto_locations):
        """
        Spawns the pedestrians at the sampled locations and makes them
        complete a trajectory to the corresponding location in the goto
        locations.

        Returns the actors spawned.
        """
        actors = []
        for location, destination in zip(sampled_locations, goto_locations):
            # Spawn the actor.
            walker_bp = random.choice(
                self._world.get_blueprint_library().filter("walker.*"))
            try:
                walker_actor = self._world.spawn_actor(
                    walker_bp, carla.Transform(location=location))
            except RuntimeError:
                print("Could not spawn the actor because of collision.")
                continue
            actors.append(walker_actor)

            # Spawn the controller.
            walker_controller_bp = self._world.get_blueprint_library().find(
                'controller.ai.walker')
            walker_controller_actor = self._world.spawn_actor(
                walker_controller_bp, carla.Transform(), walker_actor)

            self._world.wait_for_tick()

            # Choose a location and make the pedestrian move there.
            walker_controller_actor.start()
            walker_controller_actor.go_to_location(destination)
            walker_controller_actor.set_max_speed(1.4)

        return actors

    def _initialize_actors(self, config):
        """
        Initializes the pedestrians in the scenario.
        """
        # Initialize all the pedestrians in the scene.
        if self._num_walkers > len(LEFT_PEDESTRIAN_LOCATIONS) + len(
                RIGHT_PEDESTRIAN_LOCATIONS):
            raise ValueError(
                "The number of walkers requested ({}) is greater than the "
                "number of unique pedestrian locations ({}).".format(
                    self._num_walkers,
                    len(LEFT_PEDESTRIAN_LOCATIONS) +
                    len(RIGHT_PEDESTRIAN_LOCATIONS)))

        left_locations, right_locations = [], []
        # To ensure that there is determinism across runs, and still be able
        # to use random.sample
        random.seed(0)
        # Only spawn pedestrians closest to the car.
        sorted_left_locations = sorted(LEFT_PEDESTRIAN_LOCATIONS,
                                       key=lambda loc: -loc.x)
        sorted_right_locations = sorted(RIGHT_PEDESTRIAN_LOCATIONS,
                                        key=lambda loc: -loc.x)
        left_locations = sorted_left_locations[:self._num_walkers // 2]
        right_locations = sorted_right_locations[:self._num_walkers // 2]

        self.other_actors.extend(
            self.spawn_pedestrians(
                right_locations,
                random.sample(RIGHT_PEDESTRIAN_LOCATIONS,
                              len(right_locations))))
        self.other_actors.extend(
            self.spawn_pedestrians(
                left_locations,
                random.sample(LEFT_PEDESTRIAN_LOCATIONS, len(left_locations))))

        # Set all the traffic lights in the world to green.
        for actor in self._world.get_actors():
            if actor.type_id == "traffic.traffic_light":
                actor.set_state(carla.TrafficLightState.Green)
                actor.freeze(True)

    def _create_test_criteria(self):
        criteria = []
        # Do no add the simulation time constraint when running in debug mode.
        if not self.debug_mode:
            # The scenario should run for 50 simulation time seconds.
            timely_arrival = MaxSimTimeTest(self.ego_vehicles[0],
                                            30,
                                            terminate_on_failure=True)
            criteria.append(timely_arrival)
        return criteria

    def _create_behavior(self):
        """
        The scenario involves setting up a set of pedestrians walking
        on the sidewalk. The ego vehicle drives forward on the street.
        """
        # Define the endcondition.
        endcondition = py_trees.composites.Parallel(
            "Waiting for end position",
            policy=py_trees.common.ParallelPolicy.SUCCESS_ON_ALL)
        endcondition.add_child(
            StandStill(self.ego_vehicles[0], name="StandStill"))

        # Define the behavior tree.
        sequence = py_trees.composites.Sequence(
            "TrackPedestrians Behavior Tree")
        sequence.add_child(
            InTriggerDistanceToLocation(
                self.ego_vehicles[0],
                self._reference_waypoint.transform.location -
                carla.Location(x=self._driving_distance), 10))
        sequence.add_child(endcondition)
        for actor in self.other_actors:
            sequence.add_child(ActorDestroy(actor))

        return sequence

    def __del__(self):
        """
        Remove all actors upon deletion
        """
        self.remove_all_actors()


class ERDOSPedestrianCrossing(BasicScenario):
    """
    This class sets up the scenario where the ego vehicle needs to drive
    on a road, and a pedestrian crosses unexpectedly from the other side of
    the road.
    """
    def __init__(self,
                 world,
                 ego_vehicles,
                 config,
                 randomize=False,
                 debug_mode=False,
                 criteria_enable=True,
                 timeout=600000000000):
        """
        Sets up the required class variables and calls BasicScenario to
        finish setting up the scenario.
        """
        self.debug_mode = debug_mode
        self._map = CarlaDataProvider.get_map()
        self._world = CarlaDataProvider.get_world()
        self._reference_waypoint = self._map.get_waypoint(
            config.trigger_points[0].location)
        self.timeout = timeout

        # Pedestrian Config
        self._pedestrian_distance = 42
        self._pedestrian_left_translation = 5
        self._pedestrian_velocity = 3.5
        # Distance at which the pedestrian starts crossing.
        self._pedestrian_trigger_distance = 30

        # Miscellaneous Config
        self._crossing_distance = 5.5
        self._driving_distance = 70

        # Call the base class to set up the scenario.
        super(ERDOSPedestrianCrossing,
              self).__init__("ERDOSPedestrianCrossing",
                             ego_vehicles,
                             config,
                             world,
                             debug_mode,
                             criteria_enable=criteria_enable)

    @staticmethod
    def get_waypoint_in_distance(waypoint, distance):
        """
        Obtain a waypoint in a given distance from the actor's location.
        Do not stop the search on the first intersection.
        """
        traveled_distance = 0
        while traveled_distance < distance:
            waypoint_new = waypoint.next(1.0)[0]
            traveled_distance += waypoint_new.transform.location.distance(
                waypoint.transform.location)
            waypoint = waypoint_new

        return waypoint, traveled_distance

    def _initialize_actors(self, config):
        """
        Initializes the other vehicles in the scenario.
        """
        # Initialize the pedestrian.
        pedestrian_left_wp, _ = \
            ERDOSPedestrianCrossing.get_waypoint_in_distance(
                self._reference_waypoint, self._pedestrian_distance)
        self._pedestrian_left_transform = carla.Transform(
            carla.Location(
                pedestrian_left_wp.transform.location.x,
                pedestrian_left_wp.transform.location.y +
                self._pedestrian_left_translation,
                pedestrian_left_wp.transform.location.z + 15),
            carla.Rotation(pedestrian_left_wp.transform.rotation.pitch,
                           pedestrian_left_wp.transform.rotation.yaw + 90,
                           pedestrian_left_wp.transform.rotation.roll))
        pedestrian_left = CarlaDataProvider.request_new_actor(
            'walker.pedestrian.0007',
            self._pedestrian_left_transform,
            rolename='pedestrian')
        self.other_actors.append(pedestrian_left)

        # Set all the traffic lights in the world to green.
        for actor in self._world.get_actors():
            if actor.type_id == "traffic.traffic_light":
                actor.set_state(carla.TrafficLightState.Green)
                actor.freeze(True)

    def _create_behavior(self):
        # The pedestrian needs to walk to the other side of the road.
        pedestrian_crossing = py_trees.composites.Parallel(
            "Obstacle clearing road",
            policy=py_trees.common.ParallelPolicy.SUCCESS_ON_ONE)
        pedestrian_crossing.add_child(
            DriveDistance(self.other_actors[0], self._crossing_distance))
        pedestrian_crossing.add_child(
            KeepVelocity(self.other_actors[0], self._pedestrian_velocity))

        # Define the endcondition.
        endcondition = py_trees.composites.Parallel(
            "Waiting for end position",
            policy=py_trees.common.ParallelPolicy.SUCCESS_ON_ALL)
        reached_goal = InTriggerDistanceToLocation(
            self.ego_vehicles[0], self._reference_waypoint.transform.location -
            carla.Location(x=self._driving_distance), 5)
        endcondition.add_child(reached_goal)

        # Define the behavior tree.
        sequence = py_trees.composites.Sequence(
            "PedestrianCrossing Behavior Tree")
        sequence.add_child(
            InTriggerDistanceToVehicle(self.other_actors[0],
                                       self.ego_vehicles[0],
                                       self._pedestrian_trigger_distance))
        sequence.add_child(pedestrian_crossing)
        sequence.add_child(endcondition)
        sequence.add_child(ActorDestroy(self.other_actors[0]))

        return sequence

    def _create_test_criteria(self):
        """
        A list of all test criteria will be created that is later used
        in parallel behavior tree.
        """
        criteria = []
        collision_criterion = CollisionTest(self.ego_vehicles[0],
                                            terminate_on_failure=True,
                                            num_updates_after_failure=10)
        criteria.append(collision_criterion)

        # Do not add the simulation time criteria when running in debug mode.
        if not self.debug_mode:
            timely_arrival = MaxSimTimeTest(self.ego_vehicles[0],
                                            50,
                                            terminate_on_failure=True)
            criteria.append(timely_arrival)

        return criteria

    def __del__(self):
        """
        Remove all actors upon deletion
        """
        self.remove_all_actors()


class ERDOSPedestrianCrossingPaths(ERDOSPedestrianCrossing):
    def __init__(self,
                 world,
                 ego_vehicles,
                 config,
                 randomize=False,
                 debug_mode=False,
                 criteria_enable=True,
                 timeout=600000000000):
        self.debug_mode = debug_mode
        self._pedestrian_right_translation = -1.5
        super(ERDOSPedestrianCrossingPaths,
              self).__init__(world, ego_vehicles, config, randomize,
                             debug_mode, criteria_enable, timeout)

    def _initialize_actors(self, config):
        super(ERDOSPedestrianCrossingPaths, self)._initialize_actors(config)
        pedestrian_right_wp, _ = \
            ERDOSPedestrianCrossing.get_waypoint_in_distance(
                self._reference_waypoint, self._pedestrian_distance + 1)
        self._pedestrian_right_transform = carla.Transform(
            carla.Location(
                pedestrian_right_wp.transform.location.x,
                pedestrian_right_wp.transform.location.y +
                self._pedestrian_right_translation,
                pedestrian_right_wp.transform.location.z + 15),
            carla.Rotation(pedestrian_right_wp.transform.rotation.pitch,
                           pedestrian_right_wp.transform.rotation.yaw - 90,
                           pedestrian_right_wp.transform.rotation.roll))
        pedestrian_right = CarlaDataProvider.request_new_actor(
            'walker.pedestrian.0005',
            self._pedestrian_right_transform,
            rolename='pedestrian')
        self.other_actors.append(pedestrian_right)

    def _create_behavior(self):
        # The pedestrians cross the street.
        pedestrian_crossing = py_trees.composites.Parallel(
            "Obstacle clearing road",
            policy=py_trees.common.ParallelPolicy.SUCCESS_ON_ONE)
        pedestrian_crossing.add_child(
            DriveDistance(self.other_actors[0], self._crossing_distance))
        pedestrian_crossing.add_child(
            KeepVelocity(self.other_actors[0], self._pedestrian_velocity))
        pedestrian_crossing.add_child(
            DriveDistance(self.other_actors[1], self._crossing_distance))
        pedestrian_crossing.add_child(
            KeepVelocity(self.other_actors[1], self._pedestrian_velocity))

        # Define the endcondition.
        endcondition = py_trees.composites.Parallel(
            "Waiting for end position",
            policy=py_trees.common.ParallelPolicy.SUCCESS_ON_ALL)
        reached_goal = InTriggerDistanceToLocation(
            self.ego_vehicles[0], self._reference_waypoint.transform.location -
            carla.Location(x=self._driving_distance), 5)
        endcondition.add_child(reached_goal)

        # Define the behavior tree.
        sequence = py_trees.composites.Sequence(
            "PedestrianCrossingPaths Behavior Tree")
        sequence.add_child(
            InTriggerDistanceToVehicle(self.other_actors[0],
                                       self.ego_vehicles[0],
                                       self._pedestrian_trigger_distance))
        sequence.add_child(pedestrian_crossing)
        sequence.add_child(endcondition)
        sequence.add_child(ActorDestroy(self.other_actors[0]))
        sequence.add_child(ActorDestroy(self.other_actors[1]))

        return sequence


class ERDOSTrafficJam(BasicScenario):
    """
    This class sets up the scenario where the ego vehicle needs to drive
    on a road, and there is a jam on both sides of the road.

    This is a single ego vehicle scenario
    """
    def __init__(self,
                 world,
                 ego_vehicles,
                 config,
                 randomize=False,
                 debug_mode=False,
                 criteria_enable=True,
                 timeout=600000000000,
                 coca_cola_van_distance=75,
                 coca_cola_van_translation=4,
                 pedestrian_distance=82,
                 pedestrian_translation=6,
                 pedestrian_velocity=3.5,
                 pedestrian_trigger_distance=50,
                 pedestrian_yaw_offset=90,
                 crossing_distance=6.5,
                 truck_bp_name='vehicle.carlamotors.carlacola'):
        """
        Sets up the required class variables and calls BasicScenario to
        finish setting up the scenario.
        """
        self.debug_mode = debug_mode
        self._map = CarlaDataProvider.get_map()
        self._world = CarlaDataProvider.get_world()
        self._reference_waypoint = self._map.get_waypoint(
            config.trigger_points[0].location)
        self.timeout = timeout

        ## Vehicles on the left side of the street.
        # Coca Cola Van Config
        self._coca_cola_van_distance = coca_cola_van_distance
        self._coca_cola_van_translation = coca_cola_van_translation
        self._truck_bp_name = truck_bp_name

        # Other vehicles in the front of coca cola van.
        self._left_blueprints = [
            "vehicle.audi.a2",
            "vehicle.chevrolet.impala",
            "vehicle.mustang.mustang",
            "vehicle.nissan.micra",
            #            "vehicle.tesla.model3", "vehicle.toyota.prius"
        ]
        self._right_blueprints = [
            "vehicle.volkswagen.t2",
            "vehicle.mini.cooperst",
            "vehicle.kawasaki.ninja",
        ]
        self._transforms = []

        # Miscellaneous Config
        self._crossing_distance = crossing_distance
        self._driving_distance = 150

        # Call the base class to set up the scenario.
        super(ERDOSTrafficJam, self).__init__("ERDOSPedestrianBehindCar",
                                              ego_vehicles,
                                              config,
                                              world,
                                              debug_mode,
                                              criteria_enable=criteria_enable)

    def _initialize_actors(self, config):
        """
        Initializes the other vehicles in the scenario.
        """
        # Initialize the coca cola truck.
        coca_cola_van_wp, _ = ERDOSPedestrianBehindCar.get_waypoint_in_distance(
            self._reference_waypoint, self._coca_cola_van_distance)
        self._coca_cola_van_transform = carla.Transform(
            carla.Location(
                coca_cola_van_wp.transform.location.x,
                coca_cola_van_wp.transform.location.y +
                self._coca_cola_van_translation,
                coca_cola_van_wp.transform.location.z + 1),
            carla.Rotation(coca_cola_van_wp.transform.rotation.pitch,
                           coca_cola_van_wp.transform.rotation.yaw + 180,
                           coca_cola_van_wp.transform.rotation.roll))
        coca_cola_van = CarlaDataProvider.request_new_actor(
            self._truck_bp_name, self._coca_cola_van_transform)
        self.other_actors.append(coca_cola_van)

        # Initialize all the other actors.
        for i, blueprint in enumerate(self._left_blueprints, 1):
            bp_wp, _ = ERDOSPedestrianBehindCar.get_waypoint_in_distance(
                self._reference_waypoint,
                self._coca_cola_van_distance - (i * 5))
            bp_transform = carla.Transform(
                carla.Location(
                    bp_wp.transform.location.x, bp_wp.transform.location.y +
                    self._coca_cola_van_translation,
                    bp_wp.transform.location.z + 1),
                carla.Rotation(bp_wp.transform.rotation.pitch,
                               bp_wp.transform.rotation.yaw + 180,
                               bp_wp.transform.rotation.roll))
            bp = CarlaDataProvider.request_new_actor(blueprint, bp_transform)
            self.other_actors.append(bp)
            self._transforms.append(bp_transform)

        for i, blueprint in enumerate(self._right_blueprints):
            offset = 0
            if i == len(self._right_blueprints) - 1:
                offset = 3
            bp_wp, _ = ERDOSPedestrianBehindCar.get_waypoint_in_distance(
                self._reference_waypoint,
                self._coca_cola_van_distance - (i * 5) - offset)
            bp_transform = carla.Transform(
                carla.Location(bp_wp.transform.location.x,
                               bp_wp.transform.location.y,
                               bp_wp.transform.location.z + 1),
                carla.Rotation(bp_wp.transform.rotation.pitch,
                               bp_wp.transform.rotation.yaw,
                               bp_wp.transform.rotation.roll))
            bp = CarlaDataProvider.request_new_actor(blueprint, bp_transform)
            self.other_actors.append(bp)
            self._transforms.append(bp_transform)

        # Set all the traffic lights in the world to green.
        for actor in self._world.get_actors():
            if actor.type_id == "traffic.traffic_light":
                actor.set_state(carla.TrafficLightState.Green)
                actor.freeze(True)

    def _create_behavior(self):
        """
        The scenario involves setting up a set of vehicles, and having a
        pedestrian run from in between the vehicles in front of the ego
        vehicle.
        """

        # First, fix the transform of the other actors in the scene.
        coca_cola_transform = ActorTransformSetter(
            self.other_actors[0], self._coca_cola_van_transform)

        transform_setters = []
        for actor, transform in zip(self.other_actors[1:], self._transforms):
            transform_setters.append(ActorTransformSetter(actor, transform))

        # Define the endcondition.
        endcondition = py_trees.composites.Parallel(
            "Waiting for end position",
            policy=py_trees.common.ParallelPolicy.SUCCESS_ON_ALL)
        reached_goal = InTriggerDistanceToLocation(
            self.ego_vehicles[0], self._transforms[-1].location, 25)
        endcondition.add_child(reached_goal)
        endcondition.add_child(
            StandStill(self.ego_vehicles[0],
                       name="StandStill",
                       duration=2,
                       epsilon=0.2))

        # Define the behavior tree.
        sequence = py_trees.composites.Sequence(
            "PedestrianBehindCar Behavior Tree")
        sequence.add_child(coca_cola_transform)
        for transform_setter in transform_setters:
            sequence.add_child(transform_setter)
        sequence.add_child(endcondition)
        sequence.add_child(ActorDestroy(self.other_actors[0]))

        return sequence

    def _create_test_criteria(self):
        """
        A list of all test criteria will be created that is later used
        in parallel behavior tree.
        """
        criteria = []
        collision_criterion = CollisionTest(self.ego_vehicles[0],
                                            terminate_on_failure=True,
                                            num_updates_after_failure=10)
        criteria.append(collision_criterion)
        # Do no add the simulation time constraint when running in debug mode.
        if not self.debug_mode:
            # The scenario should run for 50 simulation time seconds.
            timely_arrival = MaxSimTimeTest(self.ego_vehicles[0],
                                            50,
                                            terminate_on_failure=True)
            criteria.append(timely_arrival)
        return criteria

    def __del__(self):
        """
        Remove all actors upon deletion
        """
        self.remove_all_actors()
