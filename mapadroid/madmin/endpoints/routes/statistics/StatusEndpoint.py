import aiohttp_jinja2

from mapadroid.madmin.AbstractMadminRootEndpoint import expand_context
from mapadroid.madmin.endpoints.routes.statistics.AbstractStatistictsRootEndpoint import AbstractStatisticsRootEndpoint


class StatusEndpoint(AbstractStatisticsRootEndpoint):
    """
    "/status"
    """

    # TODO: Auth
    @aiohttp_jinja2.template('status.html')
    @expand_context()
    async def get(self):
        return {
            "title": "Worker status",
            "responsive": str(self._get_mad_args().madmin_noresponsive).lower()
        }