import subprocess
import sys


CONTAINER_NAME = "fastapi-container"
IMAGE_NAME = "fastapi-app:1.0"


def run_command(command):
    print(f"Running: {' '.join(command)}")

    result = subprocess.run(
        command,
        capture_output=True,
        text=True
    )

    if result.stdout:
        print(result.stdout)

    if result.stderr:
        print(result.stderr)

    return result


def container_exists():
    result = run_command([
        "docker",
        "ps",
        "-a",
        "--filter",
        f"name=^{CONTAINER_NAME}$",
        "--format",
        "{{.Names}}"
    ])

    return CONTAINER_NAME in result.stdout.splitlines()


def deploy():
    print("Starting deployment...")

    # 1. Check old container
    if container_exists():
        print(f"Existing container '{CONTAINER_NAME}' found.")

        # Stop container
        print("Stopping old container...")
        result = run_command([
            "docker",
            "stop",
            CONTAINER_NAME
        ])

        if result.returncode != 0:
            print("Failed to stop container.")
            sys.exit(1)

        # Remove container
        print("Removing old container...")
        result = run_command([
            "docker",
            "rm",
            CONTAINER_NAME
        ])

        if result.returncode != 0:
            print("Failed to remove container.")
            sys.exit(1)

    else:
        print("No existing container found.")

    # 2. Start new container
    print("Starting new container...")

    result = run_command([
        "docker",
        "run",
        "-d",
        "--name",
        CONTAINER_NAME,
        "-p",
        "8000:8000",
        IMAGE_NAME
    ])

    if result.returncode != 0:
        print("Deployment failed.")
        sys.exit(1)

    print("Deployment successful!")
    print(f"Container '{CONTAINER_NAME}' is running.")


if __name__ == "__main__":
    deploy()