import logging

FORMAT = '%(asctime)-15s %(name)s - %(levelname)s - %(message)s '
logging.basicConfig(format=FORMAT,
                    datefmt='%m-%d %H:%M',
                    level=logging.INFO,
                    filename='logs/logg_txt.log'
                    )

logger = logging.getLogger('main_application')
