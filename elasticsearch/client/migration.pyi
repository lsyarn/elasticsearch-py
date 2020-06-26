# Licensed to Elasticsearch B.V under one or more agreements.
# Elasticsearch B.V licenses this file to you under the Apache 2.0 License.
# See the LICENSE file in the project root for more information

from typing import Any, Mapping, Optional
from .utils import NamespacedClient

class MigrationClient(NamespacedClient):
    def deprecations(
        self,
        index: Optional[Any] = None,
        params: Optional[Mapping[str, Any]] = None,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Any: ...
