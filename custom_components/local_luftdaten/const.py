from datetime import timedelta

from homeassistant.const import (
    #Config
    CONF_HOST,
    CONF_NAME,
    CONF_RESOURCE,
    CONF_VERIFY_SSL,
    CONF_MONITORED_CONDITIONS,
    CONF_SCAN_INTERVAL,
    #Units of measurement
    TEMP_CELSIUS,
    PERCENTAGE,
    PRESSURE_PA,
    SIGNAL_STRENGTH_DECIBELS_MILLIWATT,
    CONCENTRATION_MICROGRAMS_PER_CUBIC_METER,
    #Device classes
    DEVICE_CLASS_TEMPERATURE,
    DEVICE_CLASS_PRESSURE,
    DEVICE_CLASS_HUMIDITY,
    DEVICE_CLASS_SIGNAL_STRENGTH
)
PPM: Final = "ppm"
PPB: Final = "ppb"
    
DOMAIN = "local_luftdaten"

DEFAULT_NAME = 'Luftdaten Sensor'
DEFAULT_RESOURCE = 'http://{}/data.json'
DEFAULT_VERIFY_SSL = True
DEFAULT_SCAN_INTERVAL = timedelta(minutes=3)

#Sensors
SENSOR_TEMPERATURE = 'temperature'
SENSOR_HUMIDITY = 'humidity'
SENSOR_BME280_TEMPERATURE = 'BME280_temperature'
SENSOR_BME280_HUMIDITY = 'BME280_humidity'
SENSOR_BME280_PRESSURE = 'BME280_pressure'
SENSOR_BMP_TEMPERATURE = 'BMP_temperature'
SENSOR_BMP_PRESSURE = 'BMP_pressure'
SENSOR_BMP280_TEMPERATURE = 'BMP280_temperature'
SENSOR_BMP280_PRESSURE = 'BMP280_pressure'
SENSOR_PM1 = 'SDS_P1'
SENSOR_PM2 = 'SDS_P2'
SENSOR_WIFI_SIGNAL = 'signal'
SENSOR_HTU21D_TEMPERATURE = 'HTU21D_temperature'
SENSOR_HTU21D_HUMIDITY = 'HTU21D_humidity'
SENSOR_SPS30_P0 = 'SPS30_P0'
SENSOR_SPS30_P2 = 'SPS30_P2'
SENSOR_SPS30_P4 = 'SPS30_P4'
SENSOR_SPS30_P1 = 'SPS30_P1'
SENSOR_PMS_P0 = 'PMS_P0'
SENSOR_PMS_P1 = 'PMS_P1'
SENSOR_PMS_P2 = 'PMS_P2'
SENSOR_HECA_TEMPERATURE = 'HECA_temperature'
SENSOR_HECA_HUMIDITY = 'HECA_humidity'
SENSOR_HPM_P1 = 'HPM_P1'
SENSOR_HPM_P2 = 'HPM_P2'
SENSOR_SHT3X_TEMPERATURE = 'SHT3X_temperature'
SENSOR_SHT3X_HUMIDITY = 'SHT3X_humidity'
SENSOR_CCS_TVOC = 'CCS_TVOC'
SENSOR_CCS_CO2 = 'CCS_CO2'

SENSOR_TYPES = {
    SENSOR_TEMPERATURE: ['Temperature', TEMP_CELSIUS, DEVICE_CLASS_TEMPERATURE],
    SENSOR_HUMIDITY: ['Humidity', PERCENTAGE, DEVICE_CLASS_HUMIDITY],
    SENSOR_BME280_TEMPERATURE: ['Temperature', TEMP_CELSIUS, DEVICE_CLASS_TEMPERATURE],
    SENSOR_BME280_HUMIDITY: ['Humidity', PERCENTAGE, DEVICE_CLASS_HUMIDITY],
    SENSOR_BME280_PRESSURE: ['Pressure', PRESSURE_PA, DEVICE_CLASS_PRESSURE],
    SENSOR_BMP_TEMPERATURE: ['Temperature', TEMP_CELSIUS, DEVICE_CLASS_TEMPERATURE],
    SENSOR_BMP_PRESSURE: ['Pressure', PRESSURE_PA, DEVICE_CLASS_PRESSURE],
    SENSOR_BMP280_TEMPERATURE: ['Temperature', TEMP_CELSIUS, DEVICE_CLASS_TEMPERATURE],
    SENSOR_BMP280_PRESSURE: ['Pressure', PRESSURE_PA, DEVICE_CLASS_PRESSURE],
    SENSOR_PM1: ['PM10', CONCENTRATION_MICROGRAMS_PER_CUBIC_METER, None],
    SENSOR_PM2: ['PM2.5', CONCENTRATION_MICROGRAMS_PER_CUBIC_METER, None],
    SENSOR_WIFI_SIGNAL: ['Wifi signal', SIGNAL_STRENGTH_DECIBELS_MILLIWATT, DEVICE_CLASS_SIGNAL_STRENGTH],
    SENSOR_HTU21D_TEMPERATURE: ['Temperature', TEMP_CELSIUS, DEVICE_CLASS_TEMPERATURE],
    SENSOR_HTU21D_HUMIDITY: ['Humidity', PERCENTAGE, DEVICE_CLASS_HUMIDITY],
    SENSOR_SPS30_P0: ['PM1', CONCENTRATION_MICROGRAMS_PER_CUBIC_METER, None],
    SENSOR_SPS30_P2: ['PM2.5', CONCENTRATION_MICROGRAMS_PER_CUBIC_METER, None],
    SENSOR_SPS30_P4: ['PM4', CONCENTRATION_MICROGRAMS_PER_CUBIC_METER, None],
    SENSOR_SPS30_P1: ['PM10', CONCENTRATION_MICROGRAMS_PER_CUBIC_METER, None],
    SENSOR_PMS_P0: ['PM1', CONCENTRATION_MICROGRAMS_PER_CUBIC_METER, None],
    SENSOR_PMS_P1: ['PM10', CONCENTRATION_MICROGRAMS_PER_CUBIC_METER, None],
    SENSOR_PMS_P2: ['PM2.5', CONCENTRATION_MICROGRAMS_PER_CUBIC_METER, None],
    SENSOR_HECA_TEMPERATURE: ['Temperature', TEMP_CELSIUS, DEVICE_CLASS_TEMPERATURE],
    SENSOR_HECA_HUMIDITY: ['Humidity', PERCENTAGE, DEVICE_CLASS_HUMIDITY],
    SENSOR_HPM_P1: ['PM10', CONCENTRATION_MICROGRAMS_PER_CUBIC_METER, None],
    SENSOR_HPM_P2: ['PM2.5', CONCENTRATION_MICROGRAMS_PER_CUBIC_METER, None],
    SENSOR_SHT3X_TEMPERATURE: ['Temperature', TEMP_CELSIUS, DEVICE_CLASS_TEMPERATURE],
    SENSOR_SHT3X_HUMIDITY: ['Humidity', PERCENTAGE, DEVICE_CLASS_HUMIDITY],
    SENSOR_CCS_CO2: ['CO2', PPM, None],
    SENSOR_CCS_TVOC: ['TVOC', PPB, None],
}
