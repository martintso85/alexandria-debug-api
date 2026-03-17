const baseUrl = "http://127.0.0.1:8000";

async function runAnalyze() {
  const payload = {
    request_id: "REQ-20260317-0001",
    project: "Dakar MLK",
    platform: "Desktop",
    issue_title: "Front USB not recognized",
    issue_description: "多個客戶反映 front USB 無法辨識，實驗室無法穩定重現，Rear USB 幾乎沒有問題。",
    symptoms: [
      "USB device not recognized",
      "Front only",
      "Rear USB almost normal"
    ],
    known_conditions: [
      "PCH to connector direct path",
      "Signal check PASS",
      "No specific USB device pattern"
    ],
    attachments: [
      {
        file_name: "Front USB not recongnized issue.pdf",
        file_id: "file_0001"
      }
    ],
    output_format: {
      language: "zh-TW",
      style: "structured",
      include_tables: true,
      include_mindmap: true,
      include_related_cases: true
    }
  };

  const response = await fetch(`${baseUrl}/api/v1/debug/analyze`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify(payload)
  });

  const result = await response.json();
  console.log(result);
}

runAnalyze().catch(console.error);
