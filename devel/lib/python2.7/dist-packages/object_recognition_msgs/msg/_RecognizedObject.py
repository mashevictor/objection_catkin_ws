# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from object_recognition_msgs/RecognizedObject.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import geometry_msgs.msg
import sensor_msgs.msg
import shape_msgs.msg
import object_recognition_msgs.msg
import std_msgs.msg

class RecognizedObject(genpy.Message):
  _md5sum = "f92c4cb29ba11f26c5f7219de97e900d"
  _type = "object_recognition_msgs/RecognizedObject"
  _has_header = True #flag to mark the presence of a Header object
  _full_text = """##################################################### HEADER ###########################################################

# The header frame corresponds to the pose frame, NOT the point_cloud frame.
Header header

################################################## OBJECT INFO #########################################################

# Contains information about the type and the position of a found object
# Some of those fields might not be filled because the used techniques do not fill them or because the user does not
# request them

# The type of the found object
object_recognition_msgs/ObjectType type

#confidence: how sure you are it is that object and not another one.
# It is between 0 and 1 and the closer to one it is the better
float32 confidence

################################################ OBJECT CLUSTERS #######################################################

# Sometimes you can extract the 3d points that belong to the object, in the frames of the original sensors
# (it is an array as you might have several sensors)
sensor_msgs/PointCloud2[] point_clouds

# Sometimes, you can only provide a bounding box/shape, even in 3d
# This is in the pose frame
shape_msgs/Mesh bounding_mesh

# Sometimes, you only have 2d input so you can't really give a pose, you just get a contour, or a box
# The last point will be linked to the first one automatically
geometry_msgs/Point[] bounding_contours

#################################################### POSE INFO #########################################################

# This is the result that everybody expects : the pose in some frame given with the input. The units are radian/meters
# as usual
geometry_msgs/PoseWithCovarianceStamped pose

================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
# 0: no frame
# 1: global frame
string frame_id

================================================================================
MSG: object_recognition_msgs/ObjectType
################################################## OBJECT ID #########################################################

# Contains information about the type of a found object. Those two sets of parameters together uniquely define an
# object

# The key of the found object: the unique identifier in the given db
string key

# The db parameters stored as a JSON/compressed YAML string. An object id does not make sense without the corresponding
# database. E.g., in object_recognition, it can look like: "{'type':'CouchDB', 'root':'http://localhost'}"
# There is no conventional format for those parameters and it's nice to keep that flexibility.
# The object_recognition_core as a generic DB type that can read those fields
# Current examples:
# For CouchDB:
#   type: 'CouchDB'
#   root: 'http://localhost:5984'
#   collection: 'object_recognition'
# For SQL household database:
#   type: 'SqlHousehold'
#   host: 'wgs36'
#   port: 5432
#   user: 'willow'
#   password: 'willow'
#   name: 'household_objects'
#   module: 'tabletop'
string db

================================================================================
MSG: sensor_msgs/PointCloud2
# This message holds a collection of N-dimensional points, which may
# contain additional information such as normals, intensity, etc. The
# point data is stored as a binary blob, its layout described by the
# contents of the "fields" array.

# The point cloud data may be organized 2d (image-like) or 1d
# (unordered). Point clouds organized as 2d images may be produced by
# camera depth sensors such as stereo or time-of-flight.

# Time of sensor data acquisition, and the coordinate frame ID (for 3d
# points).
Header header

# 2D structure of the point cloud. If the cloud is unordered, height is
# 1 and width is the length of the point cloud.
uint32 height
uint32 width

# Describes the channels and their layout in the binary data blob.
PointField[] fields

bool    is_bigendian # Is this data bigendian?
uint32  point_step   # Length of a point in bytes
uint32  row_step     # Length of a row in bytes
uint8[] data         # Actual point data, size is (row_step*height)

bool is_dense        # True if there are no invalid points

================================================================================
MSG: sensor_msgs/PointField
# This message holds the description of one point entry in the
# PointCloud2 message format.
uint8 INT8    = 1
uint8 UINT8   = 2
uint8 INT16   = 3
uint8 UINT16  = 4
uint8 INT32   = 5
uint8 UINT32  = 6
uint8 FLOAT32 = 7
uint8 FLOAT64 = 8

string name      # Name of field
uint32 offset    # Offset from start of point struct
uint8  datatype  # Datatype enumeration, see above
uint32 count     # How many elements in the field

================================================================================
MSG: shape_msgs/Mesh
# Definition of a mesh

# list of triangles; the index values refer to positions in vertices[]
MeshTriangle[] triangles

# the actual vertices that make up the mesh
geometry_msgs/Point[] vertices

================================================================================
MSG: shape_msgs/MeshTriangle
# Definition of a triangle's vertices
uint32[3] vertex_indices

================================================================================
MSG: geometry_msgs/Point
# This contains the position of a point in free space
float64 x
float64 y
float64 z

================================================================================
MSG: geometry_msgs/PoseWithCovarianceStamped
# This expresses an estimated pose with a reference coordinate frame and timestamp

Header header
PoseWithCovariance pose

================================================================================
MSG: geometry_msgs/PoseWithCovariance
# This represents a pose in free space with uncertainty.

Pose pose

# Row-major representation of the 6x6 covariance matrix
# The orientation parameters use a fixed-axis representation.
# In order, the parameters are:
# (x, y, z, rotation about X axis, rotation about Y axis, rotation about Z axis)
float64[36] covariance

================================================================================
MSG: geometry_msgs/Pose
# A representation of pose in free space, composed of position and orientation. 
Point position
Quaternion orientation

================================================================================
MSG: geometry_msgs/Quaternion
# This represents an orientation in free space in quaternion form.

float64 x
float64 y
float64 z
float64 w
"""
  __slots__ = ['header','type','confidence','point_clouds','bounding_mesh','bounding_contours','pose']
  _slot_types = ['std_msgs/Header','object_recognition_msgs/ObjectType','float32','sensor_msgs/PointCloud2[]','shape_msgs/Mesh','geometry_msgs/Point[]','geometry_msgs/PoseWithCovarianceStamped']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       header,type,confidence,point_clouds,bounding_mesh,bounding_contours,pose

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(RecognizedObject, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.type is None:
        self.type = object_recognition_msgs.msg.ObjectType()
      if self.confidence is None:
        self.confidence = 0.
      if self.point_clouds is None:
        self.point_clouds = []
      if self.bounding_mesh is None:
        self.bounding_mesh = shape_msgs.msg.Mesh()
      if self.bounding_contours is None:
        self.bounding_contours = []
      if self.pose is None:
        self.pose = geometry_msgs.msg.PoseWithCovarianceStamped()
    else:
      self.header = std_msgs.msg.Header()
      self.type = object_recognition_msgs.msg.ObjectType()
      self.confidence = 0.
      self.point_clouds = []
      self.bounding_mesh = shape_msgs.msg.Mesh()
      self.bounding_contours = []
      self.pose = geometry_msgs.msg.PoseWithCovarianceStamped()

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_get_struct_3I().pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self.type.key
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self.type.db
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      buff.write(_get_struct_f().pack(self.confidence))
      length = len(self.point_clouds)
      buff.write(_struct_I.pack(length))
      for val1 in self.point_clouds:
        _v1 = val1.header
        buff.write(_get_struct_I().pack(_v1.seq))
        _v2 = _v1.stamp
        _x = _v2
        buff.write(_get_struct_2I().pack(_x.secs, _x.nsecs))
        _x = _v1.frame_id
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.pack('<I%ss'%length, length, _x))
        _x = val1
        buff.write(_get_struct_2I().pack(_x.height, _x.width))
        length = len(val1.fields)
        buff.write(_struct_I.pack(length))
        for val2 in val1.fields:
          _x = val2.name
          length = len(_x)
          if python3 or type(_x) == unicode:
            _x = _x.encode('utf-8')
            length = len(_x)
          buff.write(struct.pack('<I%ss'%length, length, _x))
          _x = val2
          buff.write(_get_struct_IBI().pack(_x.offset, _x.datatype, _x.count))
        _x = val1
        buff.write(_get_struct_B2I().pack(_x.is_bigendian, _x.point_step, _x.row_step))
        _x = val1.data
        length = len(_x)
        # - if encoded as a list instead, serialize as bytes instead of string
        if type(_x) in [list, tuple]:
          buff.write(struct.pack('<I%sB'%length, length, *_x))
        else:
          buff.write(struct.pack('<I%ss'%length, length, _x))
        buff.write(_get_struct_B().pack(val1.is_dense))
      length = len(self.bounding_mesh.triangles)
      buff.write(_struct_I.pack(length))
      for val1 in self.bounding_mesh.triangles:
        buff.write(_get_struct_3I().pack(*val1.vertex_indices))
      length = len(self.bounding_mesh.vertices)
      buff.write(_struct_I.pack(length))
      for val1 in self.bounding_mesh.vertices:
        _x = val1
        buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.z))
      length = len(self.bounding_contours)
      buff.write(_struct_I.pack(length))
      for val1 in self.bounding_contours:
        _x = val1
        buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.z))
      _x = self
      buff.write(_get_struct_3I().pack(_x.pose.header.seq, _x.pose.header.stamp.secs, _x.pose.header.stamp.nsecs))
      _x = self.pose.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_get_struct_7d().pack(_x.pose.pose.pose.position.x, _x.pose.pose.pose.position.y, _x.pose.pose.pose.position.z, _x.pose.pose.pose.orientation.x, _x.pose.pose.pose.orientation.y, _x.pose.pose.pose.orientation.z, _x.pose.pose.pose.orientation.w))
      buff.write(_get_struct_36d().pack(*self.pose.pose.covariance))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.type is None:
        self.type = object_recognition_msgs.msg.ObjectType()
      if self.point_clouds is None:
        self.point_clouds = None
      if self.bounding_mesh is None:
        self.bounding_mesh = shape_msgs.msg.Mesh()
      if self.bounding_contours is None:
        self.bounding_contours = None
      if self.pose is None:
        self.pose = geometry_msgs.msg.PoseWithCovarianceStamped()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.header.frame_id = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.type.key = str[start:end].decode('utf-8')
      else:
        self.type.key = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.type.db = str[start:end].decode('utf-8')
      else:
        self.type.db = str[start:end]
      start = end
      end += 4
      (self.confidence,) = _get_struct_f().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.point_clouds = []
      for i in range(0, length):
        val1 = sensor_msgs.msg.PointCloud2()
        _v3 = val1.header
        start = end
        end += 4
        (_v3.seq,) = _get_struct_I().unpack(str[start:end])
        _v4 = _v3.stamp
        _x = _v4
        start = end
        end += 8
        (_x.secs, _x.nsecs,) = _get_struct_2I().unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          _v3.frame_id = str[start:end].decode('utf-8')
        else:
          _v3.frame_id = str[start:end]
        _x = val1
        start = end
        end += 8
        (_x.height, _x.width,) = _get_struct_2I().unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        val1.fields = []
        for i in range(0, length):
          val2 = sensor_msgs.msg.PointField()
          start = end
          end += 4
          (length,) = _struct_I.unpack(str[start:end])
          start = end
          end += length
          if python3:
            val2.name = str[start:end].decode('utf-8')
          else:
            val2.name = str[start:end]
          _x = val2
          start = end
          end += 9
          (_x.offset, _x.datatype, _x.count,) = _get_struct_IBI().unpack(str[start:end])
          val1.fields.append(val2)
        _x = val1
        start = end
        end += 9
        (_x.is_bigendian, _x.point_step, _x.row_step,) = _get_struct_B2I().unpack(str[start:end])
        val1.is_bigendian = bool(val1.is_bigendian)
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        val1.data = str[start:end]
        start = end
        end += 1
        (val1.is_dense,) = _get_struct_B().unpack(str[start:end])
        val1.is_dense = bool(val1.is_dense)
        self.point_clouds.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.bounding_mesh.triangles = []
      for i in range(0, length):
        val1 = shape_msgs.msg.MeshTriangle()
        start = end
        end += 12
        val1.vertex_indices = _get_struct_3I().unpack(str[start:end])
        self.bounding_mesh.triangles.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.bounding_mesh.vertices = []
      for i in range(0, length):
        val1 = geometry_msgs.msg.Point()
        _x = val1
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _get_struct_3d().unpack(str[start:end])
        self.bounding_mesh.vertices.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.bounding_contours = []
      for i in range(0, length):
        val1 = geometry_msgs.msg.Point()
        _x = val1
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _get_struct_3d().unpack(str[start:end])
        self.bounding_contours.append(val1)
      _x = self
      start = end
      end += 12
      (_x.pose.header.seq, _x.pose.header.stamp.secs, _x.pose.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.pose.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.pose.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 56
      (_x.pose.pose.pose.position.x, _x.pose.pose.pose.position.y, _x.pose.pose.pose.position.z, _x.pose.pose.pose.orientation.x, _x.pose.pose.pose.orientation.y, _x.pose.pose.pose.orientation.z, _x.pose.pose.pose.orientation.w,) = _get_struct_7d().unpack(str[start:end])
      start = end
      end += 288
      self.pose.pose.covariance = _get_struct_36d().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_3I().pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self.type.key
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self.type.db
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      buff.write(_get_struct_f().pack(self.confidence))
      length = len(self.point_clouds)
      buff.write(_struct_I.pack(length))
      for val1 in self.point_clouds:
        _v5 = val1.header
        buff.write(_get_struct_I().pack(_v5.seq))
        _v6 = _v5.stamp
        _x = _v6
        buff.write(_get_struct_2I().pack(_x.secs, _x.nsecs))
        _x = _v5.frame_id
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.pack('<I%ss'%length, length, _x))
        _x = val1
        buff.write(_get_struct_2I().pack(_x.height, _x.width))
        length = len(val1.fields)
        buff.write(_struct_I.pack(length))
        for val2 in val1.fields:
          _x = val2.name
          length = len(_x)
          if python3 or type(_x) == unicode:
            _x = _x.encode('utf-8')
            length = len(_x)
          buff.write(struct.pack('<I%ss'%length, length, _x))
          _x = val2
          buff.write(_get_struct_IBI().pack(_x.offset, _x.datatype, _x.count))
        _x = val1
        buff.write(_get_struct_B2I().pack(_x.is_bigendian, _x.point_step, _x.row_step))
        _x = val1.data
        length = len(_x)
        # - if encoded as a list instead, serialize as bytes instead of string
        if type(_x) in [list, tuple]:
          buff.write(struct.pack('<I%sB'%length, length, *_x))
        else:
          buff.write(struct.pack('<I%ss'%length, length, _x))
        buff.write(_get_struct_B().pack(val1.is_dense))
      length = len(self.bounding_mesh.triangles)
      buff.write(_struct_I.pack(length))
      for val1 in self.bounding_mesh.triangles:
        buff.write(val1.vertex_indices.tostring())
      length = len(self.bounding_mesh.vertices)
      buff.write(_struct_I.pack(length))
      for val1 in self.bounding_mesh.vertices:
        _x = val1
        buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.z))
      length = len(self.bounding_contours)
      buff.write(_struct_I.pack(length))
      for val1 in self.bounding_contours:
        _x = val1
        buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.z))
      _x = self
      buff.write(_get_struct_3I().pack(_x.pose.header.seq, _x.pose.header.stamp.secs, _x.pose.header.stamp.nsecs))
      _x = self.pose.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_get_struct_7d().pack(_x.pose.pose.pose.position.x, _x.pose.pose.pose.position.y, _x.pose.pose.pose.position.z, _x.pose.pose.pose.orientation.x, _x.pose.pose.pose.orientation.y, _x.pose.pose.pose.orientation.z, _x.pose.pose.pose.orientation.w))
      buff.write(self.pose.pose.covariance.tostring())
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.type is None:
        self.type = object_recognition_msgs.msg.ObjectType()
      if self.point_clouds is None:
        self.point_clouds = None
      if self.bounding_mesh is None:
        self.bounding_mesh = shape_msgs.msg.Mesh()
      if self.bounding_contours is None:
        self.bounding_contours = None
      if self.pose is None:
        self.pose = geometry_msgs.msg.PoseWithCovarianceStamped()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.header.frame_id = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.type.key = str[start:end].decode('utf-8')
      else:
        self.type.key = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.type.db = str[start:end].decode('utf-8')
      else:
        self.type.db = str[start:end]
      start = end
      end += 4
      (self.confidence,) = _get_struct_f().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.point_clouds = []
      for i in range(0, length):
        val1 = sensor_msgs.msg.PointCloud2()
        _v7 = val1.header
        start = end
        end += 4
        (_v7.seq,) = _get_struct_I().unpack(str[start:end])
        _v8 = _v7.stamp
        _x = _v8
        start = end
        end += 8
        (_x.secs, _x.nsecs,) = _get_struct_2I().unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          _v7.frame_id = str[start:end].decode('utf-8')
        else:
          _v7.frame_id = str[start:end]
        _x = val1
        start = end
        end += 8
        (_x.height, _x.width,) = _get_struct_2I().unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        val1.fields = []
        for i in range(0, length):
          val2 = sensor_msgs.msg.PointField()
          start = end
          end += 4
          (length,) = _struct_I.unpack(str[start:end])
          start = end
          end += length
          if python3:
            val2.name = str[start:end].decode('utf-8')
          else:
            val2.name = str[start:end]
          _x = val2
          start = end
          end += 9
          (_x.offset, _x.datatype, _x.count,) = _get_struct_IBI().unpack(str[start:end])
          val1.fields.append(val2)
        _x = val1
        start = end
        end += 9
        (_x.is_bigendian, _x.point_step, _x.row_step,) = _get_struct_B2I().unpack(str[start:end])
        val1.is_bigendian = bool(val1.is_bigendian)
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        val1.data = str[start:end]
        start = end
        end += 1
        (val1.is_dense,) = _get_struct_B().unpack(str[start:end])
        val1.is_dense = bool(val1.is_dense)
        self.point_clouds.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.bounding_mesh.triangles = []
      for i in range(0, length):
        val1 = shape_msgs.msg.MeshTriangle()
        start = end
        end += 12
        val1.vertex_indices = numpy.frombuffer(str[start:end], dtype=numpy.uint32, count=3)
        self.bounding_mesh.triangles.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.bounding_mesh.vertices = []
      for i in range(0, length):
        val1 = geometry_msgs.msg.Point()
        _x = val1
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _get_struct_3d().unpack(str[start:end])
        self.bounding_mesh.vertices.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.bounding_contours = []
      for i in range(0, length):
        val1 = geometry_msgs.msg.Point()
        _x = val1
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _get_struct_3d().unpack(str[start:end])
        self.bounding_contours.append(val1)
      _x = self
      start = end
      end += 12
      (_x.pose.header.seq, _x.pose.header.stamp.secs, _x.pose.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.pose.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.pose.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 56
      (_x.pose.pose.pose.position.x, _x.pose.pose.pose.position.y, _x.pose.pose.pose.position.z, _x.pose.pose.pose.orientation.x, _x.pose.pose.pose.orientation.y, _x.pose.pose.pose.orientation.z, _x.pose.pose.pose.orientation.w,) = _get_struct_7d().unpack(str[start:end])
      start = end
      end += 288
      self.pose.pose.covariance = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=36)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_IBI = None
def _get_struct_IBI():
    global _struct_IBI
    if _struct_IBI is None:
        _struct_IBI = struct.Struct("<IBI")
    return _struct_IBI
_struct_B = None
def _get_struct_B():
    global _struct_B
    if _struct_B is None:
        _struct_B = struct.Struct("<B")
    return _struct_B
_struct_f = None
def _get_struct_f():
    global _struct_f
    if _struct_f is None:
        _struct_f = struct.Struct("<f")
    return _struct_f
_struct_36d = None
def _get_struct_36d():
    global _struct_36d
    if _struct_36d is None:
        _struct_36d = struct.Struct("<36d")
    return _struct_36d
_struct_3I = None
def _get_struct_3I():
    global _struct_3I
    if _struct_3I is None:
        _struct_3I = struct.Struct("<3I")
    return _struct_3I
_struct_7d = None
def _get_struct_7d():
    global _struct_7d
    if _struct_7d is None:
        _struct_7d = struct.Struct("<7d")
    return _struct_7d
_struct_B2I = None
def _get_struct_B2I():
    global _struct_B2I
    if _struct_B2I is None:
        _struct_B2I = struct.Struct("<B2I")
    return _struct_B2I
_struct_2I = None
def _get_struct_2I():
    global _struct_2I
    if _struct_2I is None:
        _struct_2I = struct.Struct("<2I")
    return _struct_2I
_struct_3d = None
def _get_struct_3d():
    global _struct_3d
    if _struct_3d is None:
        _struct_3d = struct.Struct("<3d")
    return _struct_3d
