.PHONY: rpm clean

VERSION ?= 0.7
BUILD_NUMBER ?= 1
SOURCE = jpcap-$(VERSION).tar.gz
TOPDIR = /tmp/jpcap-rpm
PWD = $(shell pwd)

rpm: $(SOURCE)
        @rpmbuild -v -bb \
                        --define "_sourcedir $(PWD)" \
                        --define "_rpmdir $(PWD)" \
                        --define "_topdir $(TOPDIR)" \
                        --define "version $(VERSION)" \
                        --define "build_number $(BUILD_NUMBER)" \
                        jpcap.spec

$(SOURCE):
        @spectool \
                        --define "version $(VERSION)" \
                        -g jpcap.spec

clean:
        @rm -rf $(TOPDIR) x86_64
        @rm -f $(SOURCE)

