from openupgradelib import openupgrade


@openupgrade.migrate(use_env=True)
def migrate(env, version):
    """
    The objective of this is delete the original view form the module how bring the functionality
    adding in the previous commit
    """
    self.env.ref('stock_ux.view_move_line_form').unlink()
    l10n_latam_use_checkbooks = env['ir.ui.view'].search([('arch_db', 'like', 'payment_status'), ('name', 'ilike', 'stock.move.line')])
    env['ir.ui.view'].search([('inherit_id', 'in', l10n_latam_use_checkbooks.ids)]).unlink()
    l10n_latam_use_checkbooks.unlink()
