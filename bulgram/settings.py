BOT_NAME = 'bulgram'

SPIDER_MODULES = ['bulgram.spiders']
NEWSPIDER_MODULE = 'bulgram.spiders'
FEED_EXPORT_ENCODING = 'utf-8'
LOG_LEVEL = 'ERROR'
DOWNLOAD_DELAY = 0

ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {
	'bulgram.pipelines.BulgramPipeline': 100,

}