import machine
import math
import time
import utime
import dht
from time import sleep
from imu import MPU6050
import DS1307

LED = machine.Pin("LED", machine.Pin.OUT)
LED.on()

gas_adc = machine.ADC(26)
ldr_adc = machine.ADC(27)
temp_adc = machine.ADC(28)

ADC_MAX = 65535
VREF = 3.3

def read_voltage(adc):
    raw = adc.read_u16()
    voltage = raw / ADC_MAX * VREF
    return voltage

def scale_to_5V(voltage):
    return voltage * (5.0 / 3.3)

def read_gas_ppm():
    v_measured = read_voltage(gas_adc)
    v_sensor = scale_to_5V(v_measured)
    ppm = (v_sensor / 5.0) * 400
    return ppm

def read_lux():
    v_measured = read_voltage(ldr_adc)
    v_sensor = scale_to_5V(v_measured)
    if v_sensor >= 5.0:
        v_sensor = 5.0 - 0.001
    resistance = 2000 * v_sensor / (1 - v_sensor / 5.0)
    GAMMA = 0.7
    RL10 = 50
    lux = (RL10 * 1e3 * (10 ** GAMMA) / resistance) ** (1.0 / GAMMA)
    return lux

def read_ntc_temperature():
    v_measured = read_voltage(temp_adc)
    if v_measured <= 0:
        return None
    R_fixed = 10000.0
    R_thermistor = v_measured * R_fixed / (VREF - v_measured)
    BETA = 3950.0
    T0 = 298.15
    R0 = 10000.0
    try:
        tempK = 1.0 / ((1.0 / T0) + (1.0 / BETA) * math.log(R_thermistor / R0))
        tempC = tempK - 273.15
    except Exception as e:
        tempC = None
    return tempC

dht_sensor = dht.DHT22(machine.Pin(16))

def read_dht():
    try:
        dht_sensor.measure()
        return dht_sensor.temperature(), dht_sensor.humidity()
    except Exception:
        return None, None

i2c = machine.I2C(0, sda=machine.Pin(4), scl=machine.Pin(5), freq=400000)

imu = MPU6050(i2c, 1)

rtc = DS1307.DS1307(0x68, i2c)

def read_rtc():
    return rtc.datetime

while True:
    gas_ppm = read_gas_ppm()
    lux = read_lux()
    ntc_temp = read_ntc_temperature()
    
    dht_temp, dht_hum = read_dht()
    
    ax = round(imu.accel.x, 2)
    ay = round(imu.accel.y, 2)
    az = round(imu.accel.z, 2)
    gx = round(imu.gyro.x, 2)
    gy = round(imu.gyro.y, 2)
    gz = round(imu.gyro.z, 2)
    mpu_temp = round(imu.temperature, 2)
    
    rtc_data = read_rtc()
    
    print("Gas Sensor (MQ2): {:.1f} ppm".format(gas_ppm))
    print("Photoresistor (LDR): {:.1f} lux".format(lux))
    if ntc_temp is None:
        print("NTC Temperature: N/A")
    else:
        print("NTC Temperature: {:.2f} °C".format(ntc_temp))
    print("MPU6050: ax={:.2f}, ay={:.2f}, az={:.2f}, gyro: x={:.2f}, y={:.2f}, z={:.2f}, Temp={:.2f} °C".format(ax, ay, az, gx, gy, gz, mpu_temp))
    if rtc_data:
        print("RTC: {}-{}-{} {}:{}:{}".format(*rtc_data))
    else:
        print("RTC: N/A")
    if dht_temp is not None:
        print("DHT22: Temp={:.2f} °C, Humidity={:.2f}%".format(dht_temp, dht_hum))
    else:
        print("DHT22: Failed to read")
    print("-" * 50)
    
    time.sleep(0.2)
