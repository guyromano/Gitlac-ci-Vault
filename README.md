## Infinity Home Assignment:

---

### The project for the Infinity assignment includes:

1) A pipeline for dockerized Python application with build (the image), test (connectivity using cURL), and delivery (upload to GitLab container registry) stages.
2) A Vault server for managing a secret. The secret is presented on the result page of the app.

---

### How to use the project?

* First, contact the admin (Guy Romano) for the GitLab server URL (no static IP was used for this project).
* Clone the repository to your local desktop, and commit some changes to the code of the app. The pipeline will initiate automatically with any commit pushed to GitLab's repository.
* Once the pipeline is finished, the new Docker image will be available on GitLab container registry.

---

### How it works? (Technical details)

* GitLab is running the pipeline on a remote GitLab Runner server. The runner is dockerized and bound with the server's Docker socket. With this architecture, every stage of the pipeline is running a container with a Docker image, outside of the runner's container for the stage execution only (Docker out of Docker).
* Before the building of the application's image, GitLab Runner is using Vault API for logging in (with AppRole authentication method), reading the secret managed by Vault, and exporting the secret as an environment variable.
* While the building of the application's image, the secret is passed to the image as a build-time argument and defined as an environment variable for the container's environment.
* After the building of the application's image, the image is tagged as "test" and pushed to GitLab container registry.
* At the test stage, the image is pulled from the registry, the container is built, and the application is tested for connectivity using cURL.
* At the delivery stage, the image is pulled again from the registry, the image is tagged with the commit SHA number and with the label "latest", and pushed again to the registry.
* After the delivery, the runner is cleaned from all the temporary Docker images (test, SHA) and left only with the "latest" image for later observation.
