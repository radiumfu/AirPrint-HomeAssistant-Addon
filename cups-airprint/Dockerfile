# syntax=docker/dockerfile:1
ARG BUILD_FROM=ghcr.io/home-assistant/amd64-base:latest
FROM ${BUILD_FROM}


# Add required packages (Alpine base image is used by HA base)
RUN apk add --no-cache \
cups cups-client cups-filters \
avahi dbus avahi-tools \
py3-pip py3-pycups \
ghostscript gutenprint hplip \
# Extra drivers for broader compatibility
brlaser foomatic-db foomatic-db-engine \
epson-inkjet-printer-escpr ricoh-ppds \
# utilities
bash coreutils shadow tzdata curl jq \
&& mkdir -p /var/run/cups /run/dbus /etc/avahi/services /data/ppd


# Copy rootfs (s6-overlay is already in HA base image)
COPY rootfs /


# Ensure scripts are executable
RUN chmod +x \
/etc/cont-init.d/* \
/etc/services.d/*/run \
/etc/services.d/*/finish \
/usr/local/bin/airprint-generate.py


# Expose CUPS (optional when using ingress-only)
EXPOSE 631


# S6 handles process supervision; no CMD needed