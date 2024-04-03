INSTANCE_NAMES = [
  {'InstanceName': 'Pie64', 'Owner': 'Quin'}, 
  {'InstanceName': 'Pie64_4', 'Owner': 'Quin'}, 
  {'InstanceName': 'Pie64_5', 'Owner': 'Quin'}, 
  {'InstanceName': 'Pie64_6', 'Owner': 'Quin'}, 
  {'InstanceName': 'Pie64_7', 'Owner': 'Quin'}, 
  {'InstanceName': 'Pie64_8', 'Owner': 'Quin'}, 
  {'InstanceName': 'Pie64_9', 'Owner': 'Quin'}, 
  {'InstanceName': 'Pie64_10', 'Owner': 'Quin'}, 
  {'InstanceName': 'Pie64_11', 'Owner': 'Quin'}, 
  {'InstanceName': 'Pie64_12', 'Owner': 'Quin'}, 
  {'InstanceName': 'Pie64_13', 'Owner': 'Quin'}, 
  {'InstanceName': 'Pie64_15', 'Owner': 'Quin'}, 
  {'InstanceName': 'Pie64_16', 'Owner': 'Quin'}, 
  {'InstanceName': 'Pie64_17', 'Owner': 'Quin'}, 
  {'InstanceName': 'Pie64_18', 'Owner': 'Quin'}, 
  {'InstanceName': 'Pie64_19', 'Owner': 'Quin'}, 
  {'InstanceName': 'Pie64_20', 'Owner': 'Quin'}, 
  {'InstanceName': 'Pie64_21', 'Owner': 'Quin'}, 
  {'InstanceName': 'Pie64_22', 'Owner': 'Quin'}
]

class Instance():
  def __init__(self, instanceID = 0):
    if instanceID >= len(INSTANCE_NAMES):
      instanceID = 0
    instance = INSTANCE_NAMES[instanceID]
    self.InstanceName = instance['InstanceName']
    self.InstanceOwner = instance['Owner']
