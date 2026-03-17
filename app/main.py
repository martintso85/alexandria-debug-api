from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI(title="Alexandria LL Debug API", version="1.0.0")
app = FastAPI(title="Alexandria LL Debug API", version="1.0.0")


class Attachment(BaseModel):
    file_name: str
    file_id: str

class OutputFormat(BaseModel):
    language: str = "zh-TW"
    style: str = "structured"
    include_tables: bool = True
    include_mindmap: bool = True
    include_related_cases: bool = True

class AnalyzeRequest(BaseModel):
    request_id: str
    project: str
    platform: Optional[str] = None
    issue_title: str
    issue_description: str
    symptoms: List[str] = []
    known_conditions: List[str] = []
    attachments: List[Attachment] = []
    output_format: OutputFormat = OutputFormat()

@app.get("/")
def root():
    return {
        "service": "Alexandria LL Debug API",
        "version": "1.0.0",
        "status": "ok"
    }

@app.post("/api/v1/debug/analyze")
def analyze_debug_issue(req: AnalyzeRequest):
    return {
        "request_id": req.request_id,
        "status": "success",
        "message": "analysis completed",
        "data": {
            "issue_summary": f"{req.issue_title} 已完成初步分析",
            "chapters": [
                {
                    "chapter_no": 1,
                    "title": "問題敘述",
                    "type": "bullet",
                    "content": [req.issue_description]
                },
                {
                    "chapter_no": 2,
                    "title": "症狀整理",
                    "type": "bullet",
                    "content": req.symptoms
                },
                {
                    "chapter_no": 3,
                    "title": "已知條件",
                    "type": "bullet",
                    "content": req.known_conditions
                }
            ],
            "action_items": [
                "建立 NG/PASS A-B 測試矩陣",
                "收集波形、版本與批次資訊",
                "比對相似案例"
            ]
        },
        "error": None
    }

@app.post("/api/v1/debug/parse-document")
def parse_document(payload: dict):
    file_id = payload.get("file_id", "")
    parse_mode = payload.get("parse_mode", "qa_structured")
    return {
        "status": "success",
        "message": "parse completed",
        "data": {
            "file_id": file_id,
            "parse_mode": parse_mode,
            "qa_count": 5,
            "sections": [
                {"qa_no": 1, "title": "初始問題"},
                {"qa_no": 2, "title": "補充條件"},
                {"qa_no": 3, "title": "進一步收斂"},
                {"qa_no": 4, "title": "驗證與反證"},
                {"qa_no": 5, "title": "最終結論"}
            ]
        },
        "error": None
    }
