FROM python:3.12.2-bullseye

ENV DEBIAN_FRONTEND=noninteractive
RUN apt update && \
    apt install git fonts-ipaexfont build-essential -y

# ARG USERNAME=dockeruser
# RUN useradd ${USERNAME} --create-home
# USER ${USERNAME}

WORKDIR /tmp/python-venv

### Using Rye ###
# RUN curl -sSf https://rye-up.com/get | RYE_NO_AUTO_INSTALL=1 RYE_INSTALL_OPTION="--yes" bash
# # ENV RYE_PATH=/home/${USERNAME}/.rye/shims
# ENV RYE_PATH=/root/.rye/shims
# ENV PATH=${RYE_PATH}:${PATH}
# RUN --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
#     --mount=type=bind,source=.python-version,target=.python-version \
#     rye sync --no-dev

### Using uv ###
RUN curl -LsSf https://astral.sh/uv/install.sh | sh
# ENV UV_PATH=/home/${USERNAME}/.cargo/bin
ENV UV_PATH=/root/.cargo/bin
ENV PATH=${UV_PATH}:${PATH}
RUN uv venv && . .venv/bin/activate
RUN --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv pip install -e .

### GPU Version ###
# FROM nvidia/cuda:12.3.2-devel-ubuntu22.04
# RUN apt install python3.10 python3-pip -y
# RUN --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
#     python3.10 -m pip install -e .

ENTRYPOINT [ "/bin/bash" ]
