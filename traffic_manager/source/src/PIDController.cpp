//Definition of class members

#include "PIDController.hpp"

namespace traffic_manager {

    PIDController::PIDController() {}

    StateEntry PIDController::stateUpdate(
        StateEntry previous_state,
        float current_velocity,
        float target_velocity,
        float angular_deviation,
        TimeInstance current_time
    ) {
        // Initializing present state
        traffic_manager::StateEntry current_state = {
            angular_deviation,
            (current_velocity - target_velocity) / target_velocity,
            current_time,
            0,
            0
        };

        // Calculating dt for 'D' and 'I' controller components
        std::chrono::duration<double> duration = current_state.time_instance - previous_state.time_instance;
        auto dt = duration.count();

        // Calculating integrals
        current_state.deviation_integral =
            angular_deviation*dt
            + previous_state.deviation_integral;
        current_state.velocity_integral = 
            dt * current_state.velocity
            + previous_state.velocity_integral;
        
        return current_state;
    }

    ActuationSignal PIDController::runStep(
        StateEntry present_state,
        StateEntry previous_state,
        std::vector<float> longitudinal_parameters,
        std::vector<float> lateral_parameters
    ) {
        // Calculating dt for updating integral component
        std::chrono::duration<double> duration = present_state.time_instance - previous_state.time_instance;
        auto dt = duration.count();

        // Longitudinal PID calculation
        float max_throttle = 0.8;
        float max_brake = 1.0;
        float expr_v =
            longitudinal_parameters[0] * present_state.velocity
            + longitudinal_parameters[1] * present_state.velocity_integral
            + longitudinal_parameters[2] * (present_state.velocity - previous_state.velocity) / dt;

        float throttle;
        float brake;

        if(expr_v < 0.0){
            throttle = std::min(std::abs(expr_v), max_throttle);
            brake = 0.0;
        }
        else{
            throttle = 0.0;
            brake = max_brake;
        }

        // Lateral PID calculation
        float steer;
        steer =
            lateral_parameters[0] * present_state.deviation
            + lateral_parameters[1] * present_state.deviation_integral
            + lateral_parameters[2] * (present_state.deviation - previous_state.deviation) / dt;
        steer = std::max(-1.0f, std::min(steer, 1.0f));

        return ActuationSignal{
            throttle,
            brake,
            steer
        };
    }

}