# generated from catkin/cmake/template/pkgConfig.cmake.in

# append elements to a list and remove existing duplicates from the list
# copied from catkin/cmake/list_append_deduplicate.cmake to keep pkgConfig
# self contained
macro(_list_append_deduplicate listname)
  if(NOT "${ARGN}" STREQUAL "")
    if(${listname})
      list(REMOVE_ITEM ${listname} ${ARGN})
    endif()
    list(APPEND ${listname} ${ARGN})
  endif()
endmacro()

# append elements to a list if they are not already in the list
# copied from catkin/cmake/list_append_unique.cmake to keep pkgConfig
# self contained
macro(_list_append_unique listname)
  foreach(_item ${ARGN})
    list(FIND ${listname} ${_item} _index)
    if(_index EQUAL -1)
      list(APPEND ${listname} ${_item})
    endif()
  endforeach()
endmacro()

# pack a list of libraries with optional build configuration keywords
# copied from catkin/cmake/catkin_libraries.cmake to keep pkgConfig
# self contained
macro(_pack_libraries_with_build_configuration VAR)
  set(${VAR} "")
  set(_argn ${ARGN})
  list(LENGTH _argn _count)
  set(_index 0)
  while(${_index} LESS ${_count})
    list(GET _argn ${_index} lib)
    if("${lib}" MATCHES "^(debug|optimized|general)$")
      math(EXPR _index "${_index} + 1")
      if(${_index} EQUAL ${_count})
        message(FATAL_ERROR "_pack_libraries_with_build_configuration() the list of libraries '${ARGN}' ends with '${lib}' which is a build configuration keyword and must be followed by a library")
      endif()
      list(GET _argn ${_index} library)
      list(APPEND ${VAR} "${lib}${CATKIN_BUILD_CONFIGURATION_KEYWORD_SEPARATOR}${library}")
    else()
      list(APPEND ${VAR} "${lib}")
    endif()
    math(EXPR _index "${_index} + 1")
  endwhile()
endmacro()

# unpack a list of libraries with optional build configuration keyword prefixes
# copied from catkin/cmake/catkin_libraries.cmake to keep pkgConfig
# self contained
macro(_unpack_libraries_with_build_configuration VAR)
  set(${VAR} "")
  foreach(lib ${ARGN})
    string(REGEX REPLACE "^(debug|optimized|general)${CATKIN_BUILD_CONFIGURATION_KEYWORD_SEPARATOR}(.+)$" "\\1;\\2" lib "${lib}")
    list(APPEND ${VAR} "${lib}")
  endforeach()
endmacro()


if(object_recognition_reconstruction_CONFIG_INCLUDED)
  return()
endif()
set(object_recognition_reconstruction_CONFIG_INCLUDED TRUE)

# set variables for source/devel/install prefixes
if("FALSE" STREQUAL "TRUE")
  set(object_recognition_reconstruction_SOURCE_PREFIX /home/victor/catkin_ws/src/reconstruction)
  set(object_recognition_reconstruction_DEVEL_PREFIX /home/victor/catkin_ws/devel)
  set(object_recognition_reconstruction_INSTALL_PREFIX "")
  set(object_recognition_reconstruction_PREFIX ${object_recognition_reconstruction_DEVEL_PREFIX})
else()
  set(object_recognition_reconstruction_SOURCE_PREFIX "")
  set(object_recognition_reconstruction_DEVEL_PREFIX "")
  set(object_recognition_reconstruction_INSTALL_PREFIX /home/victor/catkin_ws/install)
  set(object_recognition_reconstruction_PREFIX ${object_recognition_reconstruction_INSTALL_PREFIX})
endif()

# warn when using a deprecated package
if(NOT "" STREQUAL "")
  set(_msg "WARNING: package 'object_recognition_reconstruction' is deprecated")
  # append custom deprecation text if available
  if(NOT "" STREQUAL "TRUE")
    set(_msg "${_msg} ()")
  endif()
  message("${_msg}")
endif()

# flag project as catkin-based to distinguish if a find_package()-ed project is a catkin project
set(object_recognition_reconstruction_FOUND_CATKIN_PROJECT TRUE)

if(NOT "/opt/ros/kinetic/include/opencv-3.3.1-dev;/opt/ros/kinetic/include/opencv-3.3.1-dev/opencv;/usr/local/include/pcl-1.8;/usr/include/eigen3;/usr/include;/usr/include/ni;/usr/include/openni2;/usr/local/include/vtk-6.3 " STREQUAL " ")
  set(object_recognition_reconstruction_INCLUDE_DIRS "")
  set(_include_dirs "/opt/ros/kinetic/include/opencv-3.3.1-dev;/opt/ros/kinetic/include/opencv-3.3.1-dev/opencv;/usr/local/include/pcl-1.8;/usr/include/eigen3;/usr/include;/usr/include/ni;/usr/include/openni2;/usr/local/include/vtk-6.3")
  if(NOT " " STREQUAL " ")
    set(_report "Check the issue tracker '' and consider creating a ticket if the problem has not been reported yet.")
  elseif(NOT "http://wg-perception.github.io/reconstruction/ " STREQUAL " ")
    set(_report "Check the website 'http://wg-perception.github.io/reconstruction/' for information and consider reporting the problem.")
  else()
    set(_report "Report the problem to the maintainer 'Vincent Rabaud <vincent.rabaud@gmail.com>' and request to fix the problem.")
  endif()
  foreach(idir ${_include_dirs})
    if(IS_ABSOLUTE ${idir} AND IS_DIRECTORY ${idir})
      set(include ${idir})
    elseif("${idir} " STREQUAL "include ")
      get_filename_component(include "${object_recognition_reconstruction_DIR}/../../../include" ABSOLUTE)
      if(NOT IS_DIRECTORY ${include})
        message(FATAL_ERROR "Project 'object_recognition_reconstruction' specifies '${idir}' as an include dir, which is not found.  It does not exist in '${include}'.  ${_report}")
      endif()
    else()
      message(FATAL_ERROR "Project 'object_recognition_reconstruction' specifies '${idir}' as an include dir, which is not found.  It does neither exist as an absolute directory nor in '/home/victor/catkin_ws/install/${idir}'.  ${_report}")
    endif()
    _list_append_unique(object_recognition_reconstruction_INCLUDE_DIRS ${include})
  endforeach()
endif()

set(libraries "/opt/ros/kinetic/lib/x86_64-linux-gnu/libopencv_calib3d3.so.3.3.1;/opt/ros/kinetic/lib/x86_64-linux-gnu/libopencv_core3.so.3.3.1;/opt/ros/kinetic/lib/x86_64-linux-gnu/libopencv_dnn3.so.3.3.1;/opt/ros/kinetic/lib/x86_64-linux-gnu/libopencv_features2d3.so.3.3.1;/opt/ros/kinetic/lib/x86_64-linux-gnu/libopencv_flann3.so.3.3.1;/opt/ros/kinetic/lib/x86_64-linux-gnu/libopencv_highgui3.so.3.3.1;/opt/ros/kinetic/lib/x86_64-linux-gnu/libopencv_imgcodecs3.so.3.3.1;/opt/ros/kinetic/lib/x86_64-linux-gnu/libopencv_imgproc3.so.3.3.1;/opt/ros/kinetic/lib/x86_64-linux-gnu/libopencv_ml3.so.3.3.1;/opt/ros/kinetic/lib/x86_64-linux-gnu/libopencv_objdetect3.so.3.3.1;/opt/ros/kinetic/lib/x86_64-linux-gnu/libopencv_photo3.so.3.3.1;/opt/ros/kinetic/lib/x86_64-linux-gnu/libopencv_shape3.so.3.3.1;/opt/ros/kinetic/lib/x86_64-linux-gnu/libopencv_stitching3.so.3.3.1;/opt/ros/kinetic/lib/x86_64-linux-gnu/libopencv_superres3.so.3.3.1;/opt/ros/kinetic/lib/x86_64-linux-gnu/libopencv_video3.so.3.3.1;/opt/ros/kinetic/lib/x86_64-linux-gnu/libopencv_videoio3.so.3.3.1;/opt/ros/kinetic/lib/x86_64-linux-gnu/libopencv_videostab3.so.3.3.1;/opt/ros/kinetic/lib/x86_64-linux-gnu/libopencv_viz3.so.3.3.1;/opt/ros/kinetic/lib/x86_64-linux-gnu/libopencv_aruco3.so.3.3.1;/opt/ros/kinetic/lib/x86_64-linux-gnu/libopencv_bgsegm3.so.3.3.1;/opt/ros/kinetic/lib/x86_64-linux-gnu/libopencv_bioinspired3.so.3.3.1;/opt/ros/kinetic/lib/x86_64-linux-gnu/libopencv_ccalib3.so.3.3.1;/opt/ros/kinetic/lib/x86_64-linux-gnu/libopencv_cvv3.so.3.3.1;/opt/ros/kinetic/lib/x86_64-linux-gnu/libopencv_datasets3.so.3.3.1;/opt/ros/kinetic/lib/x86_64-linux-gnu/libopencv_dpm3.so.3.3.1;/opt/ros/kinetic/lib/x86_64-linux-gnu/libopencv_face3.so.3.3.1;/opt/ros/kinetic/lib/x86_64-linux-gnu/libopencv_fuzzy3.so.3.3.1;/opt/ros/kinetic/lib/x86_64-linux-gnu/libopencv_hdf3.so.3.3.1;/opt/ros/kinetic/lib/x86_64-linux-gnu/libopencv_img_hash3.so.3.3.1;/opt/ros/kinetic/lib/x86_64-linux-gnu/libopencv_line_descriptor3.so.3.3.1;/opt/ros/kinetic/lib/x86_64-linux-gnu/libopencv_optflow3.so.3.3.1;/opt/ros/kinetic/lib/x86_64-linux-gnu/libopencv_phase_unwrapping3.so.3.3.1;/opt/ros/kinetic/lib/x86_64-linux-gnu/libopencv_plot3.so.3.3.1;/opt/ros/kinetic/lib/x86_64-linux-gnu/libopencv_reg3.so.3.3.1;/opt/ros/kinetic/lib/x86_64-linux-gnu/libopencv_rgbd3.so.3.3.1;/opt/ros/kinetic/lib/x86_64-linux-gnu/libopencv_saliency3.so.3.3.1;/opt/ros/kinetic/lib/x86_64-linux-gnu/libopencv_stereo3.so.3.3.1;/opt/ros/kinetic/lib/x86_64-linux-gnu/libopencv_structured_light3.so.3.3.1;/opt/ros/kinetic/lib/x86_64-linux-gnu/libopencv_surface_matching3.so.3.3.1;/opt/ros/kinetic/lib/x86_64-linux-gnu/libopencv_text3.so.3.3.1;/opt/ros/kinetic/lib/x86_64-linux-gnu/libopencv_tracking3.so.3.3.1;/opt/ros/kinetic/lib/x86_64-linux-gnu/libopencv_xfeatures2d3.so.3.3.1;/opt/ros/kinetic/lib/x86_64-linux-gnu/libopencv_ximgproc3.so.3.3.1;/opt/ros/kinetic/lib/x86_64-linux-gnu/libopencv_xobjdetect3.so.3.3.1;/opt/ros/kinetic/lib/x86_64-linux-gnu/libopencv_xphoto3.so.3.3.1;optimized;/usr/local/lib/libpcl_common.so;debug;/usr/local/lib/libpcl_common.so;optimized;/usr/local/lib/libpcl_octree.so;debug;/usr/local/lib/libpcl_octree.so;optimized;/usr/local/lib/libpcl_io.so;debug;/usr/local/lib/libpcl_io.so;optimized;/usr/local/lib/libpcl_stereo.so;debug;/usr/local/lib/libpcl_stereo.so;optimized;/usr/local/lib/libpcl_kdtree.so;debug;/usr/local/lib/libpcl_kdtree.so;optimized;/usr/local/lib/libpcl_search.so;debug;/usr/local/lib/libpcl_search.so;optimized;/usr/local/lib/libpcl_sample_consensus.so;debug;/usr/local/lib/libpcl_sample_consensus.so;optimized;/usr/local/lib/libpcl_filters.so;debug;/usr/local/lib/libpcl_filters.so;optimized;/usr/local/lib/libpcl_visualization.so;debug;/usr/local/lib/libpcl_visualization.so;optimized;/usr/local/lib/libpcl_outofcore.so;debug;/usr/local/lib/libpcl_outofcore.so;optimized;/usr/local/lib/libpcl_surface.so;debug;/usr/local/lib/libpcl_surface.so;optimized;/usr/local/lib/libpcl_features.so;debug;/usr/local/lib/libpcl_features.so;optimized;/usr/local/lib/libpcl_ml.so;debug;/usr/local/lib/libpcl_ml.so;optimized;/usr/local/lib/libpcl_segmentation.so;debug;/usr/local/lib/libpcl_segmentation.so;optimized;/usr/local/lib/libpcl_registration.so;debug;/usr/local/lib/libpcl_registration.so;optimized;/usr/local/lib/libpcl_recognition.so;debug;/usr/local/lib/libpcl_recognition.so;optimized;/usr/local/lib/libpcl_keypoints.so;debug;/usr/local/lib/libpcl_keypoints.so;optimized;/usr/local/lib/libpcl_tracking.so;debug;/usr/local/lib/libpcl_tracking.so;optimized;/usr/local/lib/libpcl_apps.so;debug;/usr/local/lib/libpcl_apps.so;optimized;/usr/local/lib/libpcl_gpu_containers.so;debug;/usr/local/lib/libpcl_gpu_containers.so;optimized;/usr/local/lib/libpcl_gpu_utils.so;debug;/usr/local/lib/libpcl_gpu_utils.so;optimized;/usr/local/lib/libpcl_gpu_octree.so;debug;/usr/local/lib/libpcl_gpu_octree.so;optimized;/usr/local/lib/libpcl_gpu_kinfu.so;debug;/usr/local/lib/libpcl_gpu_kinfu.so;optimized;/usr/local/lib/libpcl_gpu_kinfu_large_scale.so;debug;/usr/local/lib/libpcl_gpu_kinfu_large_scale.so;optimized;/usr/local/lib/libpcl_gpu_segmentation.so;debug;/usr/local/lib/libpcl_gpu_segmentation.so;optimized;/usr/local/lib/libpcl_gpu_features.so;debug;/usr/local/lib/libpcl_gpu_features.so;optimized;/usr/local/lib/libpcl_people.so;debug;/usr/local/lib/libpcl_people.so;/usr/lib/x86_64-linux-gnu/libboost_system.so;/usr/lib/x86_64-linux-gnu/libboost_filesystem.so;/usr/lib/x86_64-linux-gnu/libboost_thread.so;/usr/lib/x86_64-linux-gnu/libboost_date_time.so;/usr/lib/x86_64-linux-gnu/libboost_iostreams.so;/usr/lib/x86_64-linux-gnu/libboost_serialization.so;/usr/lib/x86_64-linux-gnu/libboost_chrono.so;/usr/lib/x86_64-linux-gnu/libboost_atomic.so;/usr/lib/x86_64-linux-gnu/libboost_regex.so;/usr/lib/x86_64-linux-gnu/libpthread.so;optimized;/usr/lib/x86_64-linux-gnu/libqhull.so;debug;/usr/lib/x86_64-linux-gnu/libqhull.so;/usr/lib/libOpenNI.so;/usr/lib/libOpenNI2.so;optimized;/usr/lib/x86_64-linux-gnu/libflann_cpp.so;debug;/usr/lib/x86_64-linux-gnu/libflann_cpp.so;/usr/local/lib/libvtkRenderingLIC-6.3.so.1;/usr/local/lib/libvtkIOLegacy-6.3.so.1;/usr/local/lib/libvtkCommonDataModel-6.3.so.1;/usr/local/lib/libvtkCommonMath-6.3.so.1;/usr/local/lib/libvtkCommonCore-6.3.so.1;/usr/local/lib/libvtksys-6.3.so.1;/usr/local/lib/libvtkCommonMisc-6.3.so.1;/usr/local/lib/libvtkCommonSystem-6.3.so.1;/usr/local/lib/libvtkCommonTransforms-6.3.so.1;/usr/local/lib/libvtkIOCore-6.3.so.1;/usr/local/lib/libvtkCommonExecutionModel-6.3.so.1;/usr/local/lib/libvtkzlib-6.3.so.1;/usr/local/lib/libvtkIOXML-6.3.so.1;/usr/local/lib/libvtkIOGeometry-6.3.so.1;/usr/local/lib/libvtkIOXMLParser-6.3.so.1;/usr/local/lib/libvtkexpat-6.3.so.1;/usr/local/lib/libvtkImagingSources-6.3.so.1;/usr/local/lib/libvtkImagingCore-6.3.so.1;/usr/local/lib/libvtkRenderingOpenGL-6.3.so.1;/usr/local/lib/libvtkImagingHybrid-6.3.so.1;/usr/local/lib/libvtkIOImage-6.3.so.1;/usr/local/lib/libvtkDICOMParser-6.3.so.1;/usr/local/lib/libvtkmetaio-6.3.so.1;/usr/local/lib/libvtkjpeg-6.3.so.1;/usr/local/lib/libvtkpng-6.3.so.1;/usr/local/lib/libvtktiff-6.3.so.1;/usr/local/lib/libvtkRenderingCore-6.3.so.1;/usr/local/lib/libvtkCommonColor-6.3.so.1;/usr/local/lib/libvtkFiltersExtraction-6.3.so.1;/usr/local/lib/libvtkFiltersCore-6.3.so.1;/usr/local/lib/libvtkFiltersGeneral-6.3.so.1;/usr/local/lib/libvtkCommonComputationalGeometry-6.3.so.1;/usr/local/lib/libvtkFiltersStatistics-6.3.so.1;/usr/local/lib/libvtkImagingFourier-6.3.so.1;/usr/local/lib/libvtkalglib-6.3.so.1;/usr/local/lib/libvtkFiltersGeometry-6.3.so.1;/usr/local/lib/libvtkFiltersSources-6.3.so.1;/usr/local/lib/libvtkIOVideo-6.3.so.1;/usr/local/lib/libvtksqlite-6.3.so.1;/usr/local/lib/libvtkfreetype-6.3.so.1;/usr/local/lib/libvtkIOPLY-6.3.so.1;/usr/local/lib/libvtkIOEnSight-6.3.so.1;/usr/local/lib/libvtkRenderingContext2D-6.3.so.1;/usr/local/lib/libvtkRenderingFreeType-6.3.so.1;/usr/local/lib/libvtkftgl-6.3.so.1;/usr/local/lib/libvtkjsoncpp-6.3.so.1;/usr/local/lib/libvtkInteractionWidgets-6.3.so.1;/usr/local/lib/libvtkFiltersHybrid-6.3.so.1;/usr/local/lib/libvtkFiltersModeling-6.3.so.1;/usr/local/lib/libvtkImagingGeneral-6.3.so.1;/usr/local/lib/libvtkInteractionStyle-6.3.so.1;/usr/local/lib/libvtkRenderingAnnotation-6.3.so.1;/usr/local/lib/libvtkImagingColor-6.3.so.1;/usr/local/lib/libvtkRenderingVolume-6.3.so.1;/usr/local/lib/libvtkImagingStencil-6.3.so.1;/usr/local/lib/libvtkInfovisCore-6.3.so.1;/usr/local/lib/libvtkFiltersSMP-6.3.so.1;/usr/local/lib/libvtkhdf5_hl-6.3.so.1;/usr/local/lib/libvtkhdf5-6.3.so.1;/usr/local/lib/libvtkInteractionImage-6.3.so.1;/usr/local/lib/libvtkGUISupportQtSQL-6.3.so.1;/usr/local/lib/libvtkIOSQL-6.3.so.1;/usr/local/lib/libvtkGUISupportQtWebkit-6.3.so.1;/usr/local/lib/libvtkViewsQt-6.3.so.1;/usr/local/lib/libvtkGUISupportQt-6.3.so.1;/usr/local/lib/libvtkViewsInfovis-6.3.so.1;/usr/local/lib/libvtkChartsCore-6.3.so.1;/usr/local/lib/libvtkFiltersImaging-6.3.so.1;/usr/local/lib/libvtkInfovisLayout-6.3.so.1;/usr/local/lib/libvtkRenderingLabel-6.3.so.1;/usr/local/lib/libvtkViewsCore-6.3.so.1;/usr/local/lib/libvtkIOExodus-6.3.so.1;/usr/local/lib/libvtkexoIIc-6.3.so.1;/usr/local/lib/libvtkNetCDF-6.3.so.1;/usr/local/lib/libvtkNetCDF_cxx-6.3.so.1;/usr/local/lib/libvtkRenderingContextOpenGL-6.3.so.1;/usr/local/lib/libvtkIOImport-6.3.so.1;/usr/local/lib/libvtkRenderingVolumeOpenGL-6.3.so.1;/usr/local/lib/libvtkverdict-6.3.so.1;/usr/local/lib/libvtkFiltersParallelImaging-6.3.so.1;/usr/local/lib/libvtkFiltersParallel-6.3.so.1;/usr/local/lib/libvtkParallelCore-6.3.so.1;/usr/local/lib/libvtkIOLSDyna-6.3.so.1;/usr/local/lib/libvtkTestingIOSQL-6.3.so.1;/usr/local/lib/libvtkIONetCDF-6.3.so.1;/usr/local/lib/libvtkImagingStatistics-6.3.so.1;/usr/local/lib/libvtkoggtheora-6.3.so.1;/usr/local/lib/libvtkIOMovie-6.3.so.1;/usr/local/lib/libvtkViewsContext2D-6.3.so.1;/usr/local/lib/libvtkGeovisCore-6.3.so.1;/usr/local/lib/libvtkRenderingImage-6.3.so.1;/usr/local/lib/libvtkFiltersHyperTree-6.3.so.1;/usr/local/lib/libvtkTestingRendering-6.3.so.1;/usr/local/lib/libvtkIOParallel-6.3.so.1;/usr/local/lib/libvtklibxml2-6.3.so.1;/usr/local/lib/libvtkGUISupportQtOpenGL-6.3.so.1;/usr/local/lib/libvtkRenderingLOD-6.3.so.1;/usr/local/lib/libvtkFiltersTexture-6.3.so.1;/usr/local/lib/libvtkIOParallelXML-6.3.so.1;/usr/local/lib/libvtkFiltersSelection-6.3.so.1;/usr/local/lib/libvtkRenderingQt-6.3.so.1;/usr/local/lib/libvtkFiltersProgrammable-6.3.so.1;/usr/local/lib/libvtkFiltersFlowPaths-6.3.so.1;/usr/local/lib/libvtkIOExport-6.3.so.1;/usr/local/lib/libvtkRenderingGL2PS-6.3.so.1;/usr/local/lib/libvtkgl2ps-6.3.so.1;/usr/local/lib/libvtkImagingMorphological-6.3.so.1;/usr/local/lib/libvtkFiltersGeneric-6.3.so.1;/usr/local/lib/libvtkIOInfovis-6.3.so.1;/usr/local/lib/libvtkTestingGenericBridge-6.3.so.1;/usr/local/lib/libvtkFiltersVerdict-6.3.so.1;/usr/local/lib/libvtkDomainsChemistry-6.3.so.1;/usr/local/lib/libvtkImagingMath-6.3.so.1;/usr/local/lib/libvtkIOMINC-6.3.so.1;/usr/local/lib/libvtkIOAMR-6.3.so.1;/usr/local/lib/libvtkFiltersAMR-6.3.so.1;/usr/local/lib/libvtkLocalExample-6.3.so.1")
foreach(library ${libraries})
  # keep build configuration keywords, target names and absolute libraries as-is
  if("${library}" MATCHES "^(debug|optimized|general)$")
    list(APPEND object_recognition_reconstruction_LIBRARIES ${library})
  elseif(TARGET ${library})
    list(APPEND object_recognition_reconstruction_LIBRARIES ${library})
  elseif(IS_ABSOLUTE ${library})
    list(APPEND object_recognition_reconstruction_LIBRARIES ${library})
  else()
    set(lib_path "")
    set(lib "${library}-NOTFOUND")
    # since the path where the library is found is returned we have to iterate over the paths manually
    foreach(path /home/victor/catkin_ws/install/lib;/home/victor/catkin_ws/devel/lib;/opt/ros/kinetic/lib)
      find_library(lib ${library}
        PATHS ${path}
        NO_DEFAULT_PATH NO_CMAKE_FIND_ROOT_PATH)
      if(lib)
        set(lib_path ${path})
        break()
      endif()
    endforeach()
    if(lib)
      _list_append_unique(object_recognition_reconstruction_LIBRARY_DIRS ${lib_path})
      list(APPEND object_recognition_reconstruction_LIBRARIES ${lib})
    else()
      # as a fall back for non-catkin libraries try to search globally
      find_library(lib ${library})
      if(NOT lib)
        message(FATAL_ERROR "Project '${PROJECT_NAME}' tried to find library '${library}'.  The library is neither a target nor built/installed properly.  Did you compile project 'object_recognition_reconstruction'?  Did you find_package() it before the subdirectory containing its code is included?")
      endif()
      list(APPEND object_recognition_reconstruction_LIBRARIES ${lib})
    endif()
  endif()
endforeach()

set(object_recognition_reconstruction_EXPORTED_TARGETS "")
# create dummy targets for exported code generation targets to make life of users easier
foreach(t ${object_recognition_reconstruction_EXPORTED_TARGETS})
  if(NOT TARGET ${t})
    add_custom_target(${t})
  endif()
endforeach()

set(depends "ecto;ecto_image_pipeline;ecto_pcl;object_recognition_core;opencv_candidate")
foreach(depend ${depends})
  string(REPLACE " " ";" depend_list ${depend})
  # the package name of the dependency must be kept in a unique variable so that it is not overwritten in recursive calls
  list(GET depend_list 0 object_recognition_reconstruction_dep)
  list(LENGTH depend_list count)
  if(${count} EQUAL 1)
    # simple dependencies must only be find_package()-ed once
    if(NOT ${object_recognition_reconstruction_dep}_FOUND)
      find_package(${object_recognition_reconstruction_dep} REQUIRED NO_MODULE)
    endif()
  else()
    # dependencies with components must be find_package()-ed again
    list(REMOVE_AT depend_list 0)
    find_package(${object_recognition_reconstruction_dep} REQUIRED NO_MODULE ${depend_list})
  endif()
  _list_append_unique(object_recognition_reconstruction_INCLUDE_DIRS ${${object_recognition_reconstruction_dep}_INCLUDE_DIRS})

  # merge build configuration keywords with library names to correctly deduplicate
  _pack_libraries_with_build_configuration(object_recognition_reconstruction_LIBRARIES ${object_recognition_reconstruction_LIBRARIES})
  _pack_libraries_with_build_configuration(_libraries ${${object_recognition_reconstruction_dep}_LIBRARIES})
  _list_append_deduplicate(object_recognition_reconstruction_LIBRARIES ${_libraries})
  # undo build configuration keyword merging after deduplication
  _unpack_libraries_with_build_configuration(object_recognition_reconstruction_LIBRARIES ${object_recognition_reconstruction_LIBRARIES})

  _list_append_unique(object_recognition_reconstruction_LIBRARY_DIRS ${${object_recognition_reconstruction_dep}_LIBRARY_DIRS})
  list(APPEND object_recognition_reconstruction_EXPORTED_TARGETS ${${object_recognition_reconstruction_dep}_EXPORTED_TARGETS})
endforeach()

set(pkg_cfg_extras "")
foreach(extra ${pkg_cfg_extras})
  if(NOT IS_ABSOLUTE ${extra})
    set(extra ${object_recognition_reconstruction_DIR}/${extra})
  endif()
  include(${extra})
endforeach()
