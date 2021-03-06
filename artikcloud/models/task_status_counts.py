# coding: utf-8

"""
    ARTIK Cloud API

    No descripton provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 2.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from pprint import pformat
from six import iteritems
import re


class TaskStatusCounts(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, num_failed=None, num_cancelled=None, total_devices=None, num_completed=None, num_succeeded=None):
        """
        TaskStatusCounts - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'num_failed': 'int',
            'num_cancelled': 'int',
            'total_devices': 'int',
            'num_completed': 'int',
            'num_succeeded': 'int'
        }

        self.attribute_map = {
            'num_failed': 'numFailed',
            'num_cancelled': 'numCancelled',
            'total_devices': 'totalDevices',
            'num_completed': 'numCompleted',
            'num_succeeded': 'numSucceeded'
        }

        self._num_failed = num_failed
        self._num_cancelled = num_cancelled
        self._total_devices = total_devices
        self._num_completed = num_completed
        self._num_succeeded = num_succeeded

    @property
    def num_failed(self):
        """
        Gets the num_failed of this TaskStatusCounts.
        Number failed

        :return: The num_failed of this TaskStatusCounts.
        :rtype: int
        """
        return self._num_failed

    @num_failed.setter
    def num_failed(self, num_failed):
        """
        Sets the num_failed of this TaskStatusCounts.
        Number failed

        :param num_failed: The num_failed of this TaskStatusCounts.
        :type: int
        """

        self._num_failed = num_failed

    @property
    def num_cancelled(self):
        """
        Gets the num_cancelled of this TaskStatusCounts.
        Number cancelled

        :return: The num_cancelled of this TaskStatusCounts.
        :rtype: int
        """
        return self._num_cancelled

    @num_cancelled.setter
    def num_cancelled(self, num_cancelled):
        """
        Sets the num_cancelled of this TaskStatusCounts.
        Number cancelled

        :param num_cancelled: The num_cancelled of this TaskStatusCounts.
        :type: int
        """

        self._num_cancelled = num_cancelled

    @property
    def total_devices(self):
        """
        Gets the total_devices of this TaskStatusCounts.
        Total devices

        :return: The total_devices of this TaskStatusCounts.
        :rtype: int
        """
        return self._total_devices

    @total_devices.setter
    def total_devices(self, total_devices):
        """
        Sets the total_devices of this TaskStatusCounts.
        Total devices

        :param total_devices: The total_devices of this TaskStatusCounts.
        :type: int
        """

        self._total_devices = total_devices

    @property
    def num_completed(self):
        """
        Gets the num_completed of this TaskStatusCounts.
        Number completed

        :return: The num_completed of this TaskStatusCounts.
        :rtype: int
        """
        return self._num_completed

    @num_completed.setter
    def num_completed(self, num_completed):
        """
        Sets the num_completed of this TaskStatusCounts.
        Number completed

        :param num_completed: The num_completed of this TaskStatusCounts.
        :type: int
        """

        self._num_completed = num_completed

    @property
    def num_succeeded(self):
        """
        Gets the num_succeeded of this TaskStatusCounts.
        Number succeeded

        :return: The num_succeeded of this TaskStatusCounts.
        :rtype: int
        """
        return self._num_succeeded

    @num_succeeded.setter
    def num_succeeded(self, num_succeeded):
        """
        Sets the num_succeeded of this TaskStatusCounts.
        Number succeeded

        :param num_succeeded: The num_succeeded of this TaskStatusCounts.
        :type: int
        """

        self._num_succeeded = num_succeeded

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
