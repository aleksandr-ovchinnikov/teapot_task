from time import sleep
from dotenv import load_dotenv
import database
import logging
import os

# Logging config and enviroment variable loading
logging.basicConfig(filename='teapot.log', level=logging.INFO, format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
load_dotenv(dotenv_path='.env')

class Teapot():
    def __init__(self):
        # init    

        self.volume = float(os.getenv('volume'))
        self.voltage = int(os.getenv('voltage'))
        self.temp = int(os.getenv('turn_off_temp'))

        if os.getenv('time') == None:
            self.time = round(4600 * self.volume * 100 / self.voltage / 100)
        else:
            self.time = int(os.getenv('time'))


    def run(self):
        # Process

        logging.info('Time to drink some TEAA!!!\n')
        database.create_info('Time to drink some TEAA!!!')
        current_temp = 0

        try:
            for i in range(1, self.time + 1):
                logging.info('Current temperature: {:.2f}'.format(current_temp))
                logging.info(f'Passed {i} seconds\n')
                if current_temp > self.temp:
                    break
                current_temp += self.temp/self.time
                sleep(1)

        except KeyboardInterrupt:
            logging.info("\nTeapot has been turned off")
            database.create_info('Teapot has been turned off')

        else:
            logging.info(f"Finally, after {self.time} seconds my tea is ready")
            database.create_info('Finally, after {self.time} seconds my tea is ready')

a = Teapot()
a.run()

