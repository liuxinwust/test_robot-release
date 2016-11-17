Name:           ros-indigo-aubo-robot
Version:        0.3.6
Release:        0%{?dist}
Summary:        ROS aubo_robot package

Group:          Development/Libraries
License:        BSD
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-indigo-aubo-control
Requires:       ros-indigo-aubo-description
Requires:       ros-indigo-aubo-driver
Requires:       ros-indigo-aubo-gazebo
Requires:       ros-indigo-aubo-i5-moveit-config
Requires:       ros-indigo-aubo-kinematics
Requires:       ros-indigo-aubo-msgs
Requires:       ros-indigo-aubo-new-driver
Requires:       ros-indigo-aubo-panel
Requires:       ros-indigo-aubo-trajectory
Requires:       ros-indigo-aubo-trajectory-filters
BuildRequires:  ros-indigo-catkin

%description
Description,drivers, moveit and utilities for AUBO Robot Arms.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Thu Nov 17 2016 liuxin <liuxin@our-robotics.com> - 0.3.6-0
- Autogenerated by Bloom

* Wed Nov 16 2016 liuxin <liuxin@our-robotics.com> - 0.3.4-0
- Autogenerated by Bloom

* Wed Nov 16 2016 liuxin <liuxin@our-robotics.com> - 0.3.2-0
- Autogenerated by Bloom

* Tue Nov 15 2016 liuxin <liuxin@our-robotics.com> - 0.2.3-0
- Autogenerated by Bloom

* Tue Oct 11 2016 liuxin <liuxin@our-robotics.com> - 0.2.1-0
- Autogenerated by Bloom

* Sun Oct 09 2016 liuxin <liuxin@our-robotics.com> - 0.1.6-0
- Autogenerated by Bloom

* Fri Sep 30 2016 liuxin <liuxin@our-robotics.com> - 0.1.5-2
- Autogenerated by Bloom

* Fri Sep 30 2016 liuxin <liuxin@our-robotics.com> - 0.1.5-1
- Autogenerated by Bloom

* Fri Sep 30 2016 liuxin <liuxin@our-robotics.com> - 0.1.5-0
- Autogenerated by Bloom

* Fri Sep 30 2016 liuxin <liuxin@our-robotics.com> - 0.1.4-0
- Autogenerated by Bloom

* Fri Sep 30 2016 liuxin <liuxin@our-robotics.com> - 0.1.3-0
- Autogenerated by Bloom

* Fri Sep 30 2016 liuxin <liuxin@our-robotics.com> - 0.1.2-0
- Autogenerated by Bloom

* Thu Sep 29 2016 liuxin <liuxin@our-robotics.com> - 0.1.1-6
- Autogenerated by Bloom

* Thu Sep 29 2016 liuxin <liuxin@our-robotics.com> - 0.1.1-5
- Autogenerated by Bloom

* Tue Sep 27 2016 liuxin <liuxin@our-robotics.com> - 0.1.1-4
- Autogenerated by Bloom

* Fri Sep 23 2016 liuxin <liuxin@our-robotics.com> - 0.1.1-3
- Autogenerated by Bloom

* Fri Sep 23 2016 liuxin <liuxin@our-robotics.com> - 0.1.1-2
- Autogenerated by Bloom

* Fri Sep 23 2016 liuxin <liuxin@our-robotics.com> - 0.1.1-1
- Autogenerated by Bloom

* Tue Sep 20 2016 liuxin <liuxin@our-robotics.com> - 0.1.1-0
- Autogenerated by Bloom

