#!/usr/bin/env python

import rospy
import std_srvs.srv
import dynamic_reconfigure.client #this lets you reconfigure node parameters

class mapCleaner:
    def __init__(self):
        #rospy.init_node('the_only_node', anonymous=True)
        self.srv_name = "/move_base/clear_costmaps"  # this is the full path name of the service
        self.clear_costmaps = rospy.ServiceProxy(self.srv_name, std_srvs.srv.Empty)
        self.static_layer = "/move_base/global_costmap/static_layer"
        self.static_layer_enabled = "{0}/enabled".format(self.static_layer)
        self.obs_layer = "/move_base/global_costmap/obstacle_layer"
        self.obs_layer_enabled = "{0}/enabled".format(self.obs_layer)

        self.static_client = dynamic_reconfigure.client.Client(self.static_layer, timeout=5)
        self.obs_client = dynamic_reconfigure.client.Client(self.obs_layer, timeout=5)

        self.r = rospy.Rate(5)

    def clearMapClient(self):
        try:
            rospy.wait_for_service(self.srv_name)
            self.clear_costmaps()
            return True
        except rospy.ServiceException:
            rospy.logerr("{0} service call failed: {1}".format(self.srv_name))
            return False

    def set_layers(self, enabled):
        self.static_client.update_configuration({"enabled": enabled})
        rospy.Duration(2)

        self.obs_client.update_configuration({"enabled": enabled})
        rospy.Duration(2)
        return True

    def reset_costmap_layers(self):
        self.set_layers(False)
        self.set_layers(True)
        return True

#if __name__ == "__main__":
    #clearMap = mapCleaner()
    #clearMap.clearMapClient() # this is a small clear for the area around a robot
    #full cleanser:
    #success = clearMap.reset_costmap_layers() # full map cleanser

