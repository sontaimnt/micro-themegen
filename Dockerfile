FROM archlinux:latest
RUN sudo pacman -Syu nix curl --noconfirm
RUN curl -fsSL https://get.jetpack.io/devbox | bash
RUN devbox
RUN git clone https://github.com/sontaimnt/micro-themegen
RUN cd micro-themegen
RUN python main.py
