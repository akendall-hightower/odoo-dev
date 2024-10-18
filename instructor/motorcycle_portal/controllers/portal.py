from odoo.http import route, request
from odoo.addons.portal.controllers import portal

class CustomerPortal(portal.CustomerPortal):
    def _prepare_home_portal_values(self, counters):
        values = super()._prepare_home_portal_values(counters)
        if "garage_count" in counters:
            count = request.env["motorcycle.registry"].search_count([])
            values["garage_count"] = count
        return values


    @route(["/my/garage", "/my/garage/page/<int:page>"], auth="user", website=True,)
    def my_garage(self, page=1, **kw):
        Garage = request.env["motorcycle.registry"]
        domain = []
        # Prepare pager data
        garage_count = Garage.search_count(domain)
        pager_data = portal.pager(
            url="/my/garage",
            total=garage_count,
            page=page,
            # step=self._items_per_page,
            step=10,
        )
        # Recordset according to pager and domain filter
        motorcycles = Garage.search(domain,limit=10,offset=pager_data["offset"],)
        # Prepare template values and render
        values = self._prepare_portal_layout_values()
        values.update(
            {
                "motorcycles": motorcycles,
                "page_name": "garage",
                "default_url": "/my/garage",
                "pager": pager_data,
            })
        return request.render("motorcycle_portal.my_garage",values)
   
    @route(["/my/garage/<model('motorcycle.registry'):doc>"],auth="user",website=True,)
    def portal_my_motorcycle(self, doc=None, **kw):
        return request.render("motorcycle_portal.my_motorcycle",{"doc": doc},)