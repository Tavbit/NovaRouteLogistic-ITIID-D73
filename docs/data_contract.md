# NovaRoute Data Contract v1.0

## Node
`id: str`, `type: distribution_center|intersection|client`, `name: str`, `x: float`, `y: float`.

## Edge
`from: str`, `to: str`, `distance_km: float > 0`, `time_min: float > 0`. The base graph is bidirectional.

## Delivery
`delivery_id`, `destination_id`, `package_type: box|envelope|bag`, `weight_kg`, `priority: low|normal|high`, `status: pending|delivered|cancelled`.

## Vehicle
`vehicle_id`, `name`, `capacity_kg`, `active`.

## Journey
`journey_id`, ISO `date`, `vehicle_id`, `start_node`, `delivery_ids[]`, `return_to_start`, optimization weights, status.

## AlgorithmResult
All search algorithms return: `algorithm`, `start_node`, `goal_node`, `cost_metric`, `path[]`, `distance_km`, `time_min`, `explored_nodes`, `execution_ms`, `success`, `message`.

Invalid input raises `ValueError`. A valid request with no route returns `success=false` and an empty path.
