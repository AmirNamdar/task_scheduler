# scheduling-service

<!-- assume the server and client are using the same timezone -->
<!-- assume auth is already handled -->

Scheduled -> Queued -> Running -> Completed(Success/Fail)

## API Server
- db layer
- seed
- init data
- init queue
- observability
- k8s

## Executures
<!-- handle all kind of tasks not just url but also running code -->

For readme
server
    layers
    tests
    how to run
    api docs /docs


support immediate and delayed tasks
support recurring tasks
support task priority

support task execution timeout, job that monitors running tasks

