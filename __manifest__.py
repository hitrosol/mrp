# @author: Panca Putra Pakpahan
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    "name": "Limit the MRP product only with the one has the BOM",
    "version": "16.0.1.0.0",
    "category": "MRP",
    "summary": "Limit the MRP product only with the one has the BOM",
    "author": "Panca Putra Pakpahan, Odoo Community Association (OCA)",
    "website": "https://solusiaglis.co.id",
    "license": "AGPL-3",
    "depends": ["mrp"],
    "data": [
        "views/mrp_production.xml",
    ],
    "installable": True,
}
