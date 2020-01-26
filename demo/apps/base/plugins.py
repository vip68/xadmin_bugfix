from django.urls import reverse
from django.template import loader
from xadmin.views import BaseAdminPlugin
from xadmin.plugins.utils import get_context_dict


class SetHomePagePlugin(BaseAdminPlugin):
    """设置首页"""

    def block_top_toolbar(self, context, nodes):
        context.update({
            'query_url': reverse('base:homepage'),
            'url_path': context['request'].path,
        })
        nodes.insert(0, loader.render_to_string('xadmin/blocks/model_list.top_toolbar.homepage.html',
                                                context=get_context_dict(context)))
