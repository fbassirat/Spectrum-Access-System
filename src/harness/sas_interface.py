#    Copyright 2016 SAS Project Authors. All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.
"""SAS interfaces for testing."""

import abc


class SasInterface(object):
  """WinnForum standardized interfaces.

  Includes SAS-CBSD interface and (will include) SAS-SAS interface.

  """

  __metaclass__ = abc.ABCMeta

  @abc.abstractmethod
  def Registration(self, request, ssl_cert=None, ssl_key=None):
    """SAS-CBSD Registration interface.

    Registers CBSDs.

    Request and response are both lists of dictionaries. Each dictionary
    contains all fields of a single request/response.

    Args:
      request: A dictionary with a single key-value pair where the key is
        "registrationRequest" and the value is a list of individual CBSD
        registration requests (each of which is itself a dictionary).
      ssl_cert: Path to SSL cert file, if None, will use default cert file.
      ssl_key: Path to SSL key file, if None, will use default key file.
    Returns:
      A dictionary with a single key-value pair where the key is
      "registrationResponse" and the value is a list of individual CBSD
      registration responses (each of which is itself a dictionary).
    """
    pass

  @abc.abstractmethod
  def SpectrumInquiry(self, request, ssl_cert=None, ssl_key=None):
    """SAS-CBSD SpectrumInquiry interface.

    Performs spectrum inquiry for CBSDs.

    Request and response are both lists of dictionaries. Each dictionary
    contains all fields of a single request/response.

    Args:
      request: A dictionary with a single key-value pair where the key is
        "spectrumInquiryRequest" and the value is a list of individual CBSD
        spectrum inquiry requests (each of which is itself a dictionary).
      ssl_cert: Path to SSL cert file, if None, will use default cert file.
      ssl_key: Path to SSL key file, if None, will use default key file.
    Returns:
      A dictionary with a single key-value pair where the key is
      "spectrumInquiryResponse" and the value is a list of individual CBSD
      spectrum inquiry responses (each of which is itself a dictionary).
    """
    pass

  @abc.abstractmethod
  def Grant(self, request, ssl_cert=None, ssl_key=None):
    """SAS-CBSD Grant interface.

    Request and response are both lists of dictionaries. Each dictionary
    contains all fields of a single request/response.

    Args:
      request: A dictionary with a single key-value pair where the key is
        "grantRequest" and the value is a list of individual CBSD
        grant requests (each of which is itself a dictionary).
      ssl_cert: Path to SSL cert file, if None, will use default cert file.
      ssl_key: Path to SSL key file, if None, will use default key file.
    Returns:
      A dictionary with a single key-value pair where the key is
      "grantResponse" and the value is a list of individual CBSD
      grant responses (each of which is itself a dictionary).
    """
    pass

  @abc.abstractmethod
  def Heartbeat(self, request, ssl_cert=None, ssl_key=None):
    """SAS-CBSD Heartbeat interface.

    Requests heartbeat for a grant for CBSDs.

    Request and response are both lists of dictionaries. Each dictionary
    contains all fields of a single request/response.

    Args:
      request: A dictionary with a single key-value pair where the key is
        "heartbeatRequest" and the value is a list of individual CBSD
        heartbeat requests (each of which is itself a dictionary).
      ssl_cert: Path to SSL cert file, if None, will use default cert file.
      ssl_key: Path to SSL key file, if None, will use default key file.
    Returns:
      A dictionary with a single key-value pair where the key is
      "heartbeatResponse" and the value is a list of individual CBSD
      heartbeat responses (each of which is itself a dictionary).
    """
    pass

  @abc.abstractmethod
  def Relinquishment(self, request, ssl_cert=None, ssl_key=None):
    """SAS-CBSD Relinquishment interface.

    Relinquishes grant for CBSDs.

    Request and response are both lists of dictionaries. Each dictionary
    contains all fields of a single request/response.

    Args:
      request: A dictionary with a single key-value pair where the key is
        "relinquishmentRequest" and the value is a list of individual CBSD
        relinquishment requests (each of which is itself a dictionary).
      ssl_cert: Path to SSL cert file, if None, will use default cert file.
      ssl_key: Path to SSL key file, if None, will use default key file.
    Returns:
      A dictionary with a single key-value pair where the key is
      "relinquishmentResponse" and the value is a list of individual CBSD
      relinquishment responses (each of which is itself a dictionary).
    """
    pass

  @abc.abstractmethod
  def Deregistration(self, request, ssl_cert=None, ssl_key=None):
    """SAS-CBSD Deregistration interface.

    Deregisters CBSDs.

    Request and response are both lists of dictionaries. Each dictionary
    contains all fields of a single request/response.

    Args:
      request: A dictionary with a single key-value pair where the key is
        "deregistrationRequest" and the value is a list of individual CBSD
        deregistration requests (each of which is itself a dictionary).
      ssl_cert: Path to SSL cert file, if None, will use default cert file.
      ssl_key: Path to SSL key file, if None, will use default key file.
    Returns:
      A dictionary with a single key-value pair where the key is
      "deregistrationResponse" and the value is a list of individual CBSD
      deregistration responses (each of which is itself a dictionary).
    """
    pass


class SasAdminInterface(object):
  """Minimal test control interface for the SAS under test."""

  __metaclass__ = abc.ABCMeta

  @abc.abstractmethod
  def Reset(self):
    """SAS admin interface to reset the SAS between test cases."""
    pass
