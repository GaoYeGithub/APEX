# Balancing Astronaut

I have always been interesting about the differences of our current atomsphere and the stratosphere. Balancing Astronaut will our our litte guy to help us find out, equiped with a couple sensors to record environmental and motion data to a microSD card in real time. All while indulging in a little fun desgining.

## Quick Overview

* Our little Robot 
* Runs on a microcontroller (Orpheus Pico)
* Logs timestamped sensor readings to microSD

## Collected Data

* Visual Feed (Camera)
* Timestamp (RTC)
* Ambient light (LDR)
* Accelerometer (3‑axis)
* Gyroscope (3‑axis)
* Onboard temperature (inertial sensor)
* Humidity and ambient temperature (DHT sensor)
* Gas concentration (MQ-2)

## Components

| Component                             | Purpose                                                        |
| ------------------------------------- | -------------------------------------------------------------- |
| All-Sky Camera RasPi                  | Record footages of our asent to the stratosphere               |
| Real Time Clock module (e.g., DS3231) | Provides accurate timestamps for each sensor reading           |
| Photoresistor (LDR) sensor module     | Measures ambient light level                                   |
| 6‑DoF IMU (Accel + Gyro + Temp)       | Tracks orientation, angular velocity, and internal temperature |
| Digital Humidity & Temperature (DHT)  | Reads ambient humidity and temperature                         |
| MQ-2 Gas Sensor module                | Detects flammable gases and smoke concentration                |
| microSD Card with SPI interface       | Stores logged sensor data in CSV format                        |
| Two DC motors + drivers               | Provides motion and stabilization torque                       |

## Wiring Diagram

<img src="https://hc-cdn.hel1.your-objectstorage.com/s/v3/91e87cb799fb1ce4368617d1b8cb171b833c0d70_image.png" alt="Balancing Astronaut wiring diagram" style="max-width:600px;"/>
<br>
## Timeline
| Phase                             | Status (%) |
| --------------------------------- | ---------- |
| Research & Planning               | 100%       |
| Sensor Integration                | 50%        |
| Wiring                            | 10%        |
| Final Testing & Debugging         | 0%         |
| Documentation & Demos             | 0%         |

### Initial Concept Sketches

<br>
<img src="https://hc-cdn.hel1.your-objectstorage.com/s/v3/3395f277e013d2904d56a850b92d3be2fe47cd24_image.png" alt="Concept sketch" style="max-width:400px;"/>
<br>
What we orginally planned...
