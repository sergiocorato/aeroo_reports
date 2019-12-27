# -*- coding: utf-8 -*-
# Copyright 2019 Sergio Corato <https://github.com/sergiocorato>
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).
from openupgradelib import openupgrade


xmlids_to_rename = [
    ("report_aeroo_ooo.report_mimetypes_pdf_odt",
     "report_aeroo.report_mimetypes_pdf_odt"),
    ("report_aeroo_ooo.report_mimetypes_pdf_ods",
     "report_aeroo.report_mimetypes_pdf_ods"),
    ("report_aeroo_ooo.report_mimetypes_doc_odt",
     "report_aeroo.report_mimetypes_doc_odt"),
    ("report_aeroo_ooo.report_mimetypes_xls_odt",
     "report_aeroo.report_mimetypes_xls_odt"),
    ("report_aeroo_ooo.report_mimetypes_csv_ods",
     "report_aeroo.report_mimetypes_csv_ods"),
]


def migrate(cr, version):
    openupgrade.rename_xmlids(cr, xmlids_to_rename)
