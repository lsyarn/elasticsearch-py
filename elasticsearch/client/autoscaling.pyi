# Licensed to Elasticsearch B.V under one or more agreements.
# Elasticsearch B.V licenses this file to you under the Apache 2.0 License.
# See the LICENSE file in the project root for more information

from typing import Any, Mapping, Optional
from .utils import NamespacedClient

class AutoscalingClient(NamespacedClient):
    def get_autoscaling_decision(
        self,
        params: Optional[Mapping[str, Any]] = None,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Any: ...
    def delete_autoscaling_policy(
        self,
        name: Any,
        params: Optional[Mapping[str, Any]] = None,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Any: ...
    def put_autoscaling_policy(
        self,
        name: Any,
        body: Any,
        params: Optional[Mapping[str, Any]] = None,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Any: ...
    def get_autoscaling_policy(
        self,
        name: Any,
        params: Optional[Mapping[str, Any]] = None,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Any: ...
