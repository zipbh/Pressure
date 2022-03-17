from fastapi import APIRouter, Query

from typing import Optional

from pydantic import Basemodel, StrictBool  # type: ignore

from datetime import datetime

from app.model import Reports

from dotenv import load_dotenv


load_dotenv()

get_reports = APIRouter()


class FindReports(Basemodel):
    report_id: Optional[str]
    generated_date: Optional[datetime]
    scheduled_next_report: Optional[datetime]
    responsible_engineer: Optional[str]
    report_requester: Optional[str]
    is_signed: Optional[StrictBool]
    signature_date: Optional[datetime]


@get_reports.get('/{q}', tags=['get_reports'])
async def root(q: Optional[FindReports], all_reports: StrictBool = True,
               limit: Optional[int] = 25):

    if all_reports:
        return await Reports.all(limit=limit)
    else:
        filter_query = [each for each in q if each is not None]
        return await Reports.filter(
            filter_query,
            limit=limit
        )
