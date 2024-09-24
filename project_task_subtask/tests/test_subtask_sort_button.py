import odoo.tests


class TestUi(odoo.tests.HttpCase):
    def test_01_subtask_sort_button(self):
        self.env["ir.module.module"].search(
            [("name", "=", "project_task_subtask")], limit=1
        ).state = "installed"
        self.start_tour("/web", "task_subtask", login="admin")
