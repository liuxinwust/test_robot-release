Name:           ros-kinetic-aubo-trajectory
Version:        0.3.18
Release:        0%{?dist}
Summary:        ROS aubo_trajectory package

Group:          Development/Libraries
License:        BSD
URL:            http://wiki.ros.org/aubo_trajectory
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-kinetic-actionlib
Requires:       ros-kinetic-aubo-msgs
Requires:       ros-kinetic-control-msgs
Requires:       ros-kinetic-interactive-markers
Requires:       ros-kinetic-moveit-core
Requires:       ros-kinetic-moveit-fake-controller-manager
Requires:       ros-kinetic-moveit-ros-perception
Requires:       ros-kinetic-moveit-ros-planning-interface
Requires:       ros-kinetic-pluginlib
Requires:       ros-kinetic-sensor-msgs
Requires:       ros-kinetic-std-msgs
BuildRequires:  ros-kinetic-actionlib
BuildRequires:  ros-kinetic-aubo-msgs
BuildRequires:  ros-kinetic-catkin
BuildRequires:  ros-kinetic-cmake-modules
BuildRequires:  ros-kinetic-control-msgs
BuildRequires:  ros-kinetic-interactive-markers
BuildRequires:  ros-kinetic-moveit-core
BuildRequires:  ros-kinetic-moveit-ros-perception
BuildRequires:  ros-kinetic-moveit-ros-planning-interface
BuildRequires:  ros-kinetic-pluginlib
BuildRequires:  ros-kinetic-sensor-msgs
BuildRequires:  ros-kinetic-std-msgs

%description
The aubo_trajectory package

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Tue Sep 05 2017 liuxin <liuxin@our-robotics.com> - 0.3.18-0
- Autogenerated by Bloom

