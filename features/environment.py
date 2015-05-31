# -*- coding: utf-8 -*-
import erppeek

__all__ = []
OPENERP_ARGS = ['-c', '/etc/odoo/demo_server.cfg', '--logfile', 'var/log/behave-stdout.log']



def before_all(ctx):
    server = 'http://192.168.0.8:8069'
    database = 'living_doc'
    ctx._is_context = True
    ctx.client = erppeek.Client(server, database, 'admin', 'password', verbose=ctx.config.verbose)
    ctx.conf = {'server': server,
                'db_name': database}


def before_feature(ctx, feature):
    ctx.data = {}


# Work around https://github.com/behave/behave/issues/145
def before_scenario(ctx, scenario):
    if not hasattr(ctx, 'data'):
        ctx.data = {}


def before_step(ctx, step):
    #pdb.set_trace()
    ctx._messages = []
    # Extra cleanup (should be fixed upstream?)
    ctx.table = None
    ctx.text = None


def after_step(ctx, laststep):
    #pdb.set_trace()
    if ctx._messages:
        # Flush the messages collected with puts(...)
        output = ctx.config.output
        for item in ctx._messages:
            for line in str(item).splitlines():
                output.write(u'      %s\n' % (line,))
        # output.flush()


# def after_feature(ctx, feature):


def after_scenario(ctx, scenario):
    if ctx.task:
        task_model = ctx.client.model('project.task')
        task_model.unlink([ctx.task.id])