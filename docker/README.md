
# Dockerfile for running Gigahorse

This dockerfile provides an environment in which all necessary dependencies of Gigahorse are installed in the correct versions.
The image also contains other useful packages such as `solc`.


## Building

To build the image run

```bash
docker build --progress plain -t gigahorse-env .
```


## Running docker container

To use Gigahorse it is easiest to create a shared volume, which maps the root dir of this repository to e.g. `/home/shared` inside the container.

Example:
```bash
docker run -it --name gigahorse -v .:/home/shared:rw gigahorse-env
```


## Usage

### Enter running containers shell
```bash
docker exec -it gigahorse bash
```

### Run gigahorse with custom client

Gigahorse is available as an executable in the `PATH`.

To use it with a custom client simply run:

```bash
gigahorse -C /home/shared/clients/client.dl contract.hex
```


### Some tips on Gigahorse

Running Gigahorse with a custom client the first time might take a long time, as all the datalog files need to be compiled by Souffle. 
Depending on your hardware this might also use up all the memory and crash. If that happens you can specify the number of concurrent jobs with the `-j` parameter, of which the default is 7. 
Setting this lower helps with the memory issue.

During development it is very useful to run the clients in interpreted mode, this can be done with the `-i`. 
This significantly speeds up the execution, but be aware that Gigahorse hides Souffle error messages from you when doing this, i.e. if Souffle compilation fails (e.g. due to invalid Datalog syntax) one might not immediately notice it like this. 