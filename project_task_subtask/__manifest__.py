{
    "name": """Project Task Checklist""",
    "summary": """Use checklist to be ensure that all your tasks are performed and to make easy control over them""",  # noqa: B950
    "category": """Project Management""",
    "images": ["images/checklist_main.png"],
    "version": "15.0.1.0.0",
    "author": "IT-Projects LLC",
    "support": "it@it-projects.info",
    "website": "https://github.com/it-projects-llc/misc-addons",
    "license": "LGPL-3",
    "depends": ["project"],
    "data": [
        "security/ir.model.access.csv",
        "views/project_task_subtask.xml",
        "views/assets.xml",
        "data/subscription_template.xml",
    ],
    "qweb": ["static/src/xml/templates.xml"],
    "demo": ["demo/project_task_subtask_demo.xml"],
}
