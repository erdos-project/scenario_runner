//definition of FeederCallable class members

#include "FeederCallable.hpp"

namespace traffic_manager
{
    Feedercallable::Feedercallable(
        SyncQueue<PipelineMessage>* input_queue,
        SyncQueue<PipelineMessage>* output_queue,
        SharedData* shared_data):
        PipelineCallable(input_queue, output_queue, shared_data){}
    Feedercallable::~Feedercallable(){}

    PipelineMessage Feedercallable::action (PipelineMessage message)
    {
        int delay = 500; // (micro seconds) default, good enough for 100 vehicles
        auto last_time = std::chrono::system_clock::now();
        while(true)
        {
            for (auto actor: shared_data->registered_actors)
            {
                message.setActor(actor);
                writeQueue(message);
                std::this_thread::sleep_for(std::chrono::microseconds(delay));
            }
            auto current_time = std::chrono::system_clock::now();
            std::chrono::duration<double> diff = current_time - last_time;

            if(diff.count() > 1.0) {
                last_time = current_time;
                delay = 1000000 / (shared_data->registered_actors.size() * 50);
            }
        }
        PipelineMessage empty_message;
        return empty_message;
    }
}