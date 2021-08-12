MPU6050_ADDRESS_AD0_LOW = 0x68 #address pin low (GND), default for InvenSense evaluation board
MPU6050_ADDRESS_AD0_HIGH = 0x69 #address pin high (VCC)
MPU6050_DEFAULT_ADDRESS = MPU6050_ADDRESS_AD0_LOW

MPU6050_RA_XG_OFFS_TC = 0x00 #[7] PWR_MODE, [6:1] XG_OFFS_TC, [0] OTP_BNK_VLD
MPU6050_RA_YG_OFFS_TC = 0x01 #[7] PWR_MODE, [6:1] YG_OFFS_TC, [0] OTP_BNK_VLD
MPU6050_RA_ZG_OFFS_TC = 0x02 #[7] PWR_MODE, [6:1] ZG_OFFS_TC, [0] OTP_BNK_VLD
MPU6050_RA_X_FINE_GAIN = 0x03 #[7:0] X_FINE_GAIN
MPU6050_RA_Y_FINE_GAIN = 0x04 #[7:0] Y_FINE_GAIN
MPU6050_RA_Z_FINE_GAIN = 0x05 #[7:0] Z_FINE_GAIN
MPU6050_RA_XA_OFFS_H = 0x06 #[15:0] XA_OFFS
MPU6050_RA_XA_OFFS_L_TC = 0x07
MPU6050_RA_YA_OFFS_H = 0x08 #[15:0] YA_OFFS
MPU6050_RA_YA_OFFS_L_TC = 0x09
MPU6050_RA_ZA_OFFS_H = 0x0A #[15:0] ZA_OFFS
MPU6050_RA_ZA_OFFS_L_TC = 0x0B
MPU6050_RA_XG_OFFS_USRH = 0x13 #[15:0] XG_OFFS_USR
MPU6050_RA_XG_OFFS_USRL = 0x14
MPU6050_RA_YG_OFFS_USRH = 0x15 #[15:0] YG_OFFS_USR
MPU6050_RA_YG_OFFS_USRL = 0x16
MPU6050_RA_ZG_OFFS_USRH = 0x17 #[15:0] ZG_OFFS_USR
MPU6050_RA_ZG_OFFS_USRL = 0x18
MPU6050_RA_SMPLRT_DIV = 0x19
MPU6050_RA_CONFIG = 0x1A
MPU6050_RA_GYRO_CONFIG =  0x1B
MPU6050_RA_ACCEL_CONFIG = 0x1C
MPU6050_RA_FF_THR = 0x1D
MPU6050_RA_FF_DUR = 0x1E
MPU6050_RA_MOT_THR = 0x1F
MPU6050_RA_MOT_DUR = 0x20
MPU6050_RA_ZRMOT_THR = 0x21
MPU6050_RA_ZRMOT_DUR = 0x22
MPU6050_RA_FIFO_EN = 0x23
MPU6050_RA_I2C_MST_CTRL = 0x24
MPU6050_RA_I2C_SLV0_ADDR = 0x25
MPU6050_RA_I2C_SLV0_REG = 0x26
MPU6050_RA_I2C_SLV0_CTRL = 0x27
MPU6050_RA_I2C_SLV1_ADDR = 0x28
MPU6050_RA_I2C_SLV1_REG = 0x29
MPU6050_RA_I2C_SLV1_CTRL = 0x2A
MPU6050_RA_I2C_SLV2_ADDR = 0x2B
MPU6050_RA_I2C_SLV2_REG = 0x2C
MPU6050_RA_I2C_SLV2_CTRL = 0x2D
MPU6050_RA_I2C_SLV3_ADDR = 0x2E
MPU6050_RA_I2C_SLV3_REG = 0x2F
MPU6050_RA_I2C_SLV3_CTRL = 0x30
MPU6050_RA_I2C_SLV4_ADDR = 0x31
MPU6050_RA_I2C_SLV4_REG = 0x32
MPU6050_RA_I2C_SLV4_DO =  0x33
MPU6050_RA_I2C_SLV4_CTRL = 0x34
MPU6050_RA_I2C_SLV4_DI =  0x35
MPU6050_RA_I2C_MST_STATUS = 0x36
MPU6050_RA_INT_PIN_CFG =  0x37
MPU6050_RA_INT_ENABLE = 0x38
MPU6050_RA_DMP_INT_STATUS = 0x39
MPU6050_RA_INT_STATUS = 0x3A
MPU6050_RA_ACCEL_XOUT_H = 0x3B
MPU6050_RA_ACCEL_XOUT_L = 0x3C
MPU6050_RA_ACCEL_YOUT_H = 0x3D
MPU6050_RA_ACCEL_YOUT_L = 0x3E
MPU6050_RA_ACCEL_ZOUT_H = 0x3F
MPU6050_RA_ACCEL_ZOUT_L = 0x40
MPU6050_RA_TEMP_OUT_H = 0x41
MPU6050_RA_TEMP_OUT_L = 0x42
MPU6050_RA_GYRO_XOUT_H =  0x43
MPU6050_RA_GYRO_XOUT_L =  0x44
MPU6050_RA_GYRO_YOUT_H =  0x45
MPU6050_RA_GYRO_YOUT_L =  0x46
MPU6050_RA_GYRO_ZOUT_H =  0x47
MPU6050_RA_GYRO_ZOUT_L =  0x48
MPU6050_RA_EXT_SENS_DATA_00 = 0x49
MPU6050_RA_EXT_SENS_DATA_01 = 0x4A
MPU6050_RA_EXT_SENS_DATA_02 = 0x4B
MPU6050_RA_EXT_SENS_DATA_03 = 0x4C
MPU6050_RA_EXT_SENS_DATA_04 = 0x4D
MPU6050_RA_EXT_SENS_DATA_05 = 0x4E
MPU6050_RA_EXT_SENS_DATA_06 = 0x4F
MPU6050_RA_EXT_SENS_DATA_07 = 0x50
MPU6050_RA_EXT_SENS_DATA_08 = 0x51
MPU6050_RA_EXT_SENS_DATA_09 = 0x52
MPU6050_RA_EXT_SENS_DATA_10 = 0x53
MPU6050_RA_EXT_SENS_DATA_11 = 0x54
MPU6050_RA_EXT_SENS_DATA_12 = 0x55
MPU6050_RA_EXT_SENS_DATA_13 = 0x56
MPU6050_RA_EXT_SENS_DATA_14 = 0x57
MPU6050_RA_EXT_SENS_DATA_15 = 0x58
MPU6050_RA_EXT_SENS_DATA_16 = 0x59
MPU6050_RA_EXT_SENS_DATA_17 = 0x5A
MPU6050_RA_EXT_SENS_DATA_18 = 0x5B
MPU6050_RA_EXT_SENS_DATA_19 = 0x5C
MPU6050_RA_EXT_SENS_DATA_20 = 0x5D
MPU6050_RA_EXT_SENS_DATA_21 = 0x5E
MPU6050_RA_EXT_SENS_DATA_22 = 0x5F
MPU6050_RA_EXT_SENS_DATA_23 = 0x60
MPU6050_RA_MOT_DETECT_STATUS = 0x61
MPU6050_RA_I2C_SLV0_DO =  0x63
MPU6050_RA_I2C_SLV1_DO =  0x64
MPU6050_RA_I2C_SLV2_DO =  0x65
MPU6050_RA_I2C_SLV3_DO =  0x66
MPU6050_RA_I2C_MST_DELAY_CTRL = 0x67
MPU6050_RA_SIGNAL_PATH_RESET = 0x68
MPU6050_RA_MOT_DETECT_CTRL =  0x69
MPU6050_RA_USER_CTRL = 0x6A
MPU6050_RA_PWR_MGMT_1 = 0x6B
MPU6050_RA_PWR_MGMT_2 = 0x6C
MPU6050_RA_BANK_SEL =  0x6D
MPU6050_RA_MEM_START_ADDR = 0x6E
MPU6050_RA_MEM_R_W = 0x6F
MPU6050_RA_DMP_CFG_1 = 0x70
MPU6050_RA_DMP_CFG_2 = 0x71
MPU6050_RA_FIFO_COUNTH = 0x72
MPU6050_RA_FIFO_COUNTL = 0x73
MPU6050_RA_FIFO_R_W = 0x74
MPU6050_RA_WHO_AM_I = 0x75

MPU6050_TC_PWR_MODE_BIT = 7
MPU6050_TC_OFFSET_BIT = 6
MPU6050_TC_OFFSET_LENGTH = 6
MPU6050_TC_OTP_BNK_VLD_BIT = 0

MPU6050_VDDIO_LEVEL_VLOGIC = 0
MPU6050_VDDIO_LEVEL_VDD = 1

MPU6050_CFG_EXT_SYNC_SET_BIT = 5
MPU6050_CFG_EXT_SYNC_SET_LENGTH = 3
MPU6050_CFG_DLPF_CFG_BIT = 2
MPU6050_CFG_DLPF_CFG_LENGTH = 3

MPU6050_EXT_SYNC_DISABLED = 0x0
MPU6050_EXT_SYNC_TEMP_OUT_L = 0x1
MPU6050_EXT_SYNC_GYRO_XOUT_L = 0x2
MPU6050_EXT_SYNC_GYRO_YOUT_L = 0x3
MPU6050_EXT_SYNC_GYRO_ZOUT_L = 0x4
MPU6050_EXT_SYNC_ACCEL_XOUT_L = 0x5
MPU6050_EXT_SYNC_ACCEL_YOUT_L = 0x6
MPU6050_EXT_SYNC_ACCEL_ZOUT_L = 0x7

MPU6050_DLPF_BW_256 = 0x00
MPU6050_DLPF_BW_188 = 0x01
MPU6050_DLPF_BW_98 = 0x02
MPU6050_DLPF_BW_42 = 0x03
MPU6050_DLPF_BW_20 = 0x04
MPU6050_DLPF_BW_10 = 0x05
MPU6050_DLPF_BW_5 = 0x06

MPU6050_GCONFIG_FS_SEL_BIT = 4
MPU6050_GCONFIG_FS_SEL_LENGTH = 2

MPU6050_GYRO_FS_250 = 0x00
MPU6050_GYRO_FS_500 = 0x01
MPU6050_GYRO_FS_1000 = 0x02
MPU6050_GYRO_FS_2000 = 0x03

MPU6050_ACONFIG_XA_ST_BIT = 7
MPU6050_ACONFIG_YA_ST_BIT = 6
MPU6050_ACONFIG_ZA_ST_BIT = 5
MPU6050_ACONFIG_AFS_SEL_BIT =  4
MPU6050_ACONFIG_AFS_SEL_LENGTH =  2
MPU6050_ACONFIG_ACCEL_HPF_BIT = 2
MPU6050_ACONFIG_ACCEL_HPF_LENGTH = 3

MPU6050_ACCEL_FS_2 = 0x00
MPU6050_ACCEL_FS_4 = 0x01
MPU6050_ACCEL_FS_8 = 0x02
MPU6050_ACCEL_FS_16 = 0x03

MPU6050_DHPF_RESET = 0x00
MPU6050_DHPF_5 = 0x01
MPU6050_DHPF_2P5 = 0x02
MPU6050_DHPF_1P25 = 0x03
MPU6050_DHPF_0P63 = 0x04
MPU6050_DHPF_HOLD = 0x07

MPU6050_TEMP_FIFO_EN_BIT = 7
MPU6050_XG_FIFO_EN_BIT =  6
MPU6050_YG_FIFO_EN_BIT =  5
MPU6050_ZG_FIFO_EN_BIT =  4
MPU6050_ACCEL_FIFO_EN_BIT = 3
MPU6050_SLV2_FIFO_EN_BIT = 2
MPU6050_SLV1_FIFO_EN_BIT = 1
MPU6050_SLV0_FIFO_EN_BIT = 0

MPU6050_MULT_MST_EN_BIT = 7
MPU6050_WAIT_FOR_ES_BIT = 6
MPU6050_SLV_3_FIFO_EN_BIT = 5
MPU6050_I2C_MST_P_NSR_BIT = 4
MPU6050_I2C_MST_CLK_BIT = 3
MPU6050_I2C_MST_CLK_LENGTH = 4

MPU6050_CLOCK_DIV_348 = 0x0
MPU6050_CLOCK_DIV_333 = 0x1
MPU6050_CLOCK_DIV_320 = 0x2
MPU6050_CLOCK_DIV_308 = 0x3
MPU6050_CLOCK_DIV_296 = 0x4
MPU6050_CLOCK_DIV_286 = 0x5
MPU6050_CLOCK_DIV_276 = 0x6
MPU6050_CLOCK_DIV_267 = 0x7
MPU6050_CLOCK_DIV_258 = 0x8
MPU6050_CLOCK_DIV_500 = 0x9
MPU6050_CLOCK_DIV_471 = 0xA
MPU6050_CLOCK_DIV_444 = 0xB
MPU6050_CLOCK_DIV_421 = 0xC
MPU6050_CLOCK_DIV_400 = 0xD
MPU6050_CLOCK_DIV_381 = 0xE
MPU6050_CLOCK_DIV_364 = 0xF

MPU6050_I2C_SLV_RW_BIT = 7
MPU6050_I2C_SLV_ADDR_BIT = 6
MPU6050_I2C_SLV_ADDR_LENGTH = 7
MPU6050_I2C_SLV_EN_BIT =  7
MPU6050_I2C_SLV_BYTE_SW_BIT = 6
MPU6050_I2C_SLV_REG_DIS_BIT = 5
MPU6050_I2C_SLV_GRP_BIT = 4
MPU6050_I2C_SLV_LEN_BIT = 3
MPU6050_I2C_SLV_LEN_LENGTH = 4

MPU6050_I2C_SLV4_RW_BIT =  7
MPU6050_I2C_SLV4_ADDR_BIT = 6
MPU6050_I2C_SLV4_ADDR_LENGTH = 7
MPU6050_I2C_SLV4_EN_BIT =  7
MPU6050_I2C_SLV4_INT_EN_BIT = 6
MPU6050_I2C_SLV4_REG_DIS_BIT = 5
MPU6050_I2C_SLV4_MST_DLY_BIT = 4
MPU6050_I2C_SLV4_MST_DLY_LENGTH = 5

MPU6050_MST_PASS_THROUGH_BIT = 7
MPU6050_MST_I2C_SLV4_DONE_BIT = 6
MPU6050_MST_I2C_LOST_ARB_BIT = 5
MPU6050_MST_I2C_SLV4_NACK_BIT = 4
MPU6050_MST_I2C_SLV3_NACK_BIT = 3
MPU6050_MST_I2C_SLV2_NACK_BIT = 2
MPU6050_MST_I2C_SLV1_NACK_BIT = 1
MPU6050_MST_I2C_SLV0_NACK_BIT = 0

MPU6050_INTCFG_INT_LEVEL_BIT = 7
MPU6050_INTCFG_INT_OPEN_BIT = 6
MPU6050_INTCFG_LATCH_INT_EN_BIT = 5
MPU6050_INTCFG_INT_RD_CLEAR_BIT = 4
MPU6050_INTCFG_FSYNC_INT_LEVEL_BIT = 3
MPU6050_INTCFG_FSYNC_INT_EN_BIT = 2
MPU6050_INTCFG_I2C_BYPASS_EN_BIT = 1
MPU6050_INTCFG_CLKOUT_EN_BIT = 0

MPU6050_INTMODE_ACTIVEHIGH = 0x00
MPU6050_INTMODE_ACTIVELOW = 0x01

MPU6050_INTDRV_PUSHPULL = 0x00
MPU6050_INTDRV_OPENDRAIN = 0x01

MPU6050_INTLATCH_50USPULSE = 0x00
MPU6050_INTLATCH_WAITCLEAR = 0x01

MPU6050_INTCLEAR_STATUSREAD = 0x00
MPU6050_INTCLEAR_ANYREAD = 0x01

MPU6050_INTERRUPT_FF_BIT = 7
MPU6050_INTERRUPT_MOT_BIT = 6
MPU6050_INTERRUPT_ZMOT_BIT = 5
MPU6050_INTERRUPT_FIFO_OFLOW_BIT = 4
MPU6050_INTERRUPT_I2C_MST_INT_BIT = 3
MPU6050_INTERRUPT_PLL_RDY_INT_BIT = 2
MPU6050_INTERRUPT_DMP_INT_BIT = 1
MPU6050_INTERRUPT_DATA_RDY_BIT = 0

MPU6050_DMPINT_5_BIT = 5
MPU6050_DMPINT_4_BIT = 4
MPU6050_DMPINT_3_BIT = 3
MPU6050_DMPINT_2_BIT = 2
MPU6050_DMPINT_1_BIT = 1
MPU6050_DMPINT_0_BIT = 0

MPU6050_MOTION_MOT_XNEG_BIT = 7
MPU6050_MOTION_MOT_XPOS_BIT = 6
MPU6050_MOTION_MOT_YNEG_BIT = 5
MPU6050_MOTION_MOT_YPOS_BIT = 4
MPU6050_MOTION_MOT_ZNEG_BIT = 3
MPU6050_MOTION_MOT_ZPOS_BIT = 2
MPU6050_MOTION_MOT_ZRMOT_BIT = 0

MPU6050_DELAYCTRL_DELAY_ES_SHADOW_BIT = 7
MPU6050_DELAYCTRL_I2C_SLV4_DLY_EN_BIT = 4
MPU6050_DELAYCTRL_I2C_SLV3_DLY_EN_BIT = 3
MPU6050_DELAYCTRL_I2C_SLV2_DLY_EN_BIT = 2
MPU6050_DELAYCTRL_I2C_SLV1_DLY_EN_BIT = 1
MPU6050_DELAYCTRL_I2C_SLV0_DLY_EN_BIT = 0

MPU6050_PATHRESET_GYRO_RESET_BIT = 2
MPU6050_PATHRESET_ACCEL_RESET_BIT = 1
MPU6050_PATHRESET_TEMP_RESET_BIT = 0

MPU6050_DETECT_ACCEL_ON_DELAY_BIT = 5
MPU6050_DETECT_ACCEL_ON_DELAY_LENGTH = 2
MPU6050_DETECT_FF_COUNT_BIT =  3
MPU6050_DETECT_FF_COUNT_LENGTH = 2
MPU6050_DETECT_MOT_COUNT_BIT = 1
MPU6050_DETECT_MOT_COUNT_LENGTH =  2

MPU6050_DETECT_DECREMENT_RESET = 0x0
MPU6050_DETECT_DECREMENT_1 = 0x1
MPU6050_DETECT_DECREMENT_2 = 0x2
MPU6050_DETECT_DECREMENT_4 = 0x3

MPU6050_USERCTRL_DMP_EN_BIT = 7
MPU6050_USERCTRL_FIFO_EN_BIT = 6
MPU6050_USERCTRL_I2C_MST_EN_BIT = 5
MPU6050_USERCTRL_I2C_IF_DIS_BIT = 4
MPU6050_USERCTRL_DMP_RESET_BIT = 3
MPU6050_USERCTRL_FIFO_RESET_BIT = 2
MPU6050_USERCTRL_I2C_MST_RESET_BIT = 1
MPU6050_USERCTRL_SIG_COND_RESET_BIT = 0

MPU6050_PWR1_DEVICE_RESET_BIT = 7
MPU6050_PWR1_SLEEP_BIT = 6
MPU6050_PWR1_CYCLE_BIT = 5
MPU6050_PWR1_TEMP_DIS_BIT = 3
MPU6050_PWR1_CLKSEL_BIT = 2
MPU6050_PWR1_CLKSEL_LENGTH = 3

MPU6050_CLOCK_INTERNAL = 0x00
MPU6050_CLOCK_PLL_XGYRO = 0x01
MPU6050_CLOCK_PLL_YGYRO = 0x02
MPU6050_CLOCK_PLL_ZGYRO = 0x03
MPU6050_CLOCK_PLL_EXT32K = 0x04
MPU6050_CLOCK_PLL_EXT19M = 0x05
MPU6050_CLOCK_KEEP_RESET = 0x07

MPU6050_PWR2_LP_WAKE_CTRL_BIT = 7
MPU6050_PWR2_LP_WAKE_CTRL_LENGTH = 2
MPU6050_PWR2_STBY_XA_BIT = 5
MPU6050_PWR2_STBY_YA_BIT = 4
MPU6050_PWR2_STBY_ZA_BIT = 3
MPU6050_PWR2_STBY_XG_BIT = 2
MPU6050_PWR2_STBY_YG_BIT = 1
MPU6050_PWR2_STBY_ZG_BIT = 0

MPU6050_WAKE_FREQ_1P25 =  0x0
MPU6050_WAKE_FREQ_2P5 = 0x1
MPU6050_WAKE_FREQ_5 =  0x2
MPU6050_WAKE_FREQ_10 = 0x3

MPU6050_BANKSEL_PRFTCH_EN_BIT = 6
MPU6050_BANKSEL_CFG_USER_BANK_BIT = 5
MPU6050_BANKSEL_MEM_SEL_BIT =  4
MPU6050_BANKSEL_MEM_SEL_LENGTH =  5

MPU6050_WHO_AM_I_BIT = 6
MPU6050_WHO_AM_I_LENGTH = 6

MPU6050_DMP_MEMORY_BANKS = 8
MPU6050_DMP_MEMORY_BANK_SIZE = 256
MPU6050_DMP_MEMORY_CHUNK_SIZE = 16

import smbus2

class mpu6050:

    # Global Variables
    GRAVITIY_MS2 = 9.80665
    address = None
    bus = None

    # Scale Modifiers
    ACCEL_SCALE_MODIFIER_2G = 16384.0
    ACCEL_SCALE_MODIFIER_4G = 8192.0
    ACCEL_SCALE_MODIFIER_8G = 4096.0
    ACCEL_SCALE_MODIFIER_16G = 2048.0

    GYRO_SCALE_MODIFIER_250DEG = 131.0
    GYRO_SCALE_MODIFIER_500DEG = 65.5
    GYRO_SCALE_MODIFIER_1000DEG = 32.8
    GYRO_SCALE_MODIFIER_2000DEG = 16.4

    def __init__(self, address, bus=1):
        self.address = address
        self.bus = smbus2.SMBus(bus)
        #Set clock to PLL w/ x-axis gyro
        #CLK_SEL | Clock Source
        #* --------+--------------------------------------
        #* 0       | Internal oscillator
        #* 1       | PLL with X Gyro reference
        #* 2       | PLL with Y Gyro reference
        #* 3       | PLL with Z Gyro reference
        #* 4       | PLL with external 32.768kHz reference
        #* 5       | PLL with external 19.2MHz reference
        #* 6       | Reserved
        #* 7       | Stops the clock and keeps the timing generator in reset
        self.write_bits(self.address, MPU6050_RA_PWR_MGMT_1, MPU6050_PWR1_CLKSEL_BIT, MPU6050_PWR1_CLKSEL_LENGTH, 1)
        #// GYRO_CONFIG register
        #/** Get full-scale gyroscope range.
        #* The FS_SEL parameter allows setting the full-scale range of the gyro sensors,
        #* as described in the table below.
        #*
        #* 0 = +/- 250 degrees/sec
        #* 1 = +/- 500 degrees/sec
        #* 2 = +/- 1000 degrees/sec
        #* 3 = +/- 2000 degrees/sec
        self.write_bits(self.address, MPU6050_RA_GYRO_CONFIG, MPU6050_GCONFIG_FS_SEL_BIT, MPU6050_GCONFIG_FS_SEL_LENGTH, 0)
        #** Get full-scale accelerometer range.
        #* The FS_SEL parameter allows setting the full-scale range of the accelerometer
        #* sensors, as described in the table below.
        #*
        #* 0 = +/- 2g
        #* 1 = +/- 4g
        #* 2 = +/- 8g
        #* 3 = +/- 16g

        self.write_bits(self.address, MPU6050_RA_ACCEL_CONFIG, MPU6050_ACONFIG_AFS_SEL_BIT, MPU6050_ACONFIG_AFS_SEL_LENGTH, 0)
        
        # Wake up the MPU-6050 since it starts in sleep mode
        self.write_bits(self.address, MPU6050_RA_PWR_MGMT_1, MPU6050_PWR1_SLEEP_BIT, 1, False)
        
        # CONFIG register

        #** Get external FSYNC configuration.
        #* Configures the external Frame Synchronization (FSYNC) pin sampling. An
        #* external signal connected to the FSYNC pin can be sampled by configuring
        #* EXT_SYNC_SET. Signal changes to the FSYNC pin are latched so that short
        #* strobes may be captured. The latched FSYNC signal will be sampled at the
        #* Sampling Rate, as defined in register 25. After sampling, the latch will
        #* reset to the current FSYNC signal state.
        #*
        #* The sampled value will be reported in place of the least significant bit in
        #* a sensor data register determined by the value of EXT_SYNC_SET according to
        #* the following table.
        #*
        #* <pre>
        #* EXT_SYNC_SET | FSYNC Bit Location
        #* -------------+-------------------
        #* 0            | Input disabled
        #* 1            | TEMP_OUT_L[0]
        #* 2            | GYRO_XOUT_L[0]
        #* 3            | GYRO_YOUT_L[0]
        #* 4            | GYRO_ZOUT_L[0]
        #* 5            | ACCEL_XOUT_L[0]
        #* 6            | ACCEL_YOUT_L[0]
        #* 7            | ACCEL_ZOUT_L[0]
        self.write_bits(self.address, MPU6050_RA_CONFIG, MPU6050_CFG_EXT_SYNC_SET_BIT, MPU6050_CFG_EXT_SYNC_SET_LENGTH, 0)

        # // Configure Gyro and Accelerometer
        #*          |   ACCELEROMETER    |           GYROSCOPE
        #* DLPF_CFG | Bandwidth | Delay  | Bandwidth | Delay  | Sample Rate
        #* ---------+-----------+--------+-----------+--------+-------------
        #* 0        | 260Hz     | 0ms    | 256Hz     | 0.98ms | 8kHz
        #* 1        | 184Hz     | 2.0ms  | 188Hz     | 1.9ms  | 1kHz
        #* 2        | 94Hz      | 3.0ms  | 98Hz      | 2.8ms  | 1kHz
        #* 3        | 44Hz      | 4.9ms  | 42Hz      | 4.8ms  | 1kHz
        #* 4        | 21Hz      | 8.5ms  | 20Hz      | 8.3ms  | 1kHz
        #* 5        | 10Hz      | 13.8ms | 10Hz      | 13.4ms | 1kHz
        #* 6        | 5Hz       | 19.0ms | 5Hz       | 18.6ms | 1kHz
        #* 7        |   -- Reserved --   |   -- Reserved --   | Reserved
        self.write_bits(self.address, MPU6050_RA_CONFIG, MPU6050_CFG_DLPF_CFG_BIT, MPU6050_CFG_DLPF_CFG_LENGTH, 0)

    # Deleting (Calling destructor)
    def __del__(self):
        self.bus.close()

    # I2C communication methods
    # Todo: move these to an extended smbus2 implementation

    def read_i2c_word_data(self, register):
        """Read two i2c registers and combine them.

        register -- the first register to read from.
        Returns the combined read results.
        """
        # Read the data from the registers
        high = self.bus.read_byte_data(self.address, register)
        low = self.bus.read_byte_data(self.address, register + 1)

        value = (high << 8) + low

        if value >= 0x8000:
            return -((65535 - value) + 1)
        else:
            return value

    def read_bits(self, dev_addr, reg_addr, bit_start, length):
        """ Read multiple bits from an 8-bit device register.

        :param dev_addr: I2C slave device address
        :param reg_addr: Register regAddr to read from
        :param bit_start: First bit position to read (0-7)
        :param length: length Number of bits to read (not more than 8)
        :return: Read byte value
        :rtype: int
        """

        raw_data = self.bus.read_byte_data(dev_addr, reg_addr)

        mask = ((1 << length) - 1) << (bit_start - length + 1)
        raw_data &= mask
        raw_data >>= (bit_start - length + 1)
        return raw_data

    def write_bits(self, dev_addr, reg_addr, bit_start, length, data):
        """ Write multiple bits in an 8-bit device register.

        :param dev_addr: I2C slave device address
        :param reg_addr: Register regAddr to write to
        :param bit_start: First bit position to write (0-7)
        :param length: Number of bits to write (not more than 8)
        :param data: Right-aligned value to write
        """
        # 010 value to write
        # 76543210 bit numbers
        # xxx args: bitStart = 4, length = 3
        # 00011100 mask byte
        # 10101111 original value(sample)
        # 10100011 original & ~mask
        # 10101011 masked | value

        # get current value of register
        raw_data = self.bus.read_byte_data(dev_addr, reg_addr)

        mask = ((1 << length) - 1) << (bit_start - length + 1)
        data <<= (bit_start - length + 1)  # shift data into correct position
        data &= mask  # zero all non-important bits in data
        raw_data &= ~mask  # zero all important bits in existing byte
        raw_data |= data  # combine data with existing byte
        self.bus.write_byte_data(dev_addr, reg_addr, raw_data)

    def getXFineGain(self):
        buffer = self.bus.read_byte_data(self.address,MPU6050_RA_X_FINE_GAIN)
        return buffer
    
    def getYFineGain(self):
        buffer = self.bus.read_byte_data(self.address,MPU6050_RA_Y_FINE_GAIN)
        return buffer
    
    def getZFineGain(self):
        buffer = self.bus.read_byte_data(self.address,MPU6050_RA_Z_FINE_GAIN)
        return buffer

    def setXFineGain(self, newgain):
        self.bus.write_byte_data(self.address,MPU6050_RA_X_FINE_GAIN, newgain)
        
    def setYFineGain(self, newgain):
        self.bus.write_byte_data(self.address,MPU6050_RA_Y_FINE_GAIN, newgain)
        
    def setZFineGain(self, newgain):
        self.bus.write_byte_data(self.address,MPU6050_RA_Z_FINE_GAIN, newgain)
        
    # The Gyro registers at boot up will have a default value of 0. 
    # The value of the bias inputted needs to be in +-1000dps sensitivity range.
    # This means each 1 dps =  32.8 LSB

    def getXGyroOffset(self):
        buffer = self.bus.read_word_data(self.address, MPU6050_RA_XG_OFFS_USRH, 2)
        return buffer

    def getYGyroOffset(self):
        buffer = self.bus.read_word_data(self.address, MPU6050_RA_YG_OFFS_USRH, 2)
        return buffer

    def getZGyroOffset(self):
        buffer = self.bus.read_word_data(self.address, MPU6050_RA_ZG_OFFS_USRH, 2)
        return buffer

    # The format are G in +-8G format. The register is initialized with OTP factory trim values

    def getXAcclOffset(self):
        buffer = self.bus.read_word_data(self.address, MPU6050_RA_XA_OFFS_H, 2)
        return buffer

    def getYAcclOffset(self):
        buffer = self.bus.read_word_data(self.address, MPU6050_RA_YA_OFFS_H, 2)
        return buffer

    def getZAcclOffset(self):
        buffer = self.bus.read_word_data(self.address, MPU6050_RA_ZA_OFFS_H, 2)
        return buffer

    def setXGyroOffset(self, offset):
        self.bus.write_word_data(self.address, MPU6050_RA_XG_OFFS_USRH, offset)
    
    def setYGyroOffset(self, offset):
        self.bus.write_word_data(self.address, MPU6050_RA_YG_OFFS_USRH, offset)

    def setZGyroOffset(self, offset):
        self.bus.write_word_data(self.address, MPU6050_RA_ZG_OFFS_USRH, offset)

    def setXAccelOffset(self, offset):
        self.bus.write_word_data(self.address, MPU6050_RA_XA_OFFS_H, offset)

    def setYAccelOffset(self, offset):
        self.bus.write_word_data(self.address, MPU6050_RA_YA_OFFS_H, offset)

    def setZAccelOffset(self, offset):
        self.bus.write_word_data(self.address, MPU6050_RA_ZA_OFFS_H, offset)

    # MPU-6050 Methods

    def get_external_frame_sync(self):
        """ Get external FSYNC configuration.

          Configures the external Frame Synchronization (FSYNC) pin sampling. An
          external signal connected to the FSYNC pin can be sampled by configuring
          EXT_SYNC_SET. Signal changes to the FSYNC pin are latched so that short
          strobes may be captured. The latched FSYNC signal will be sampled at the
          Sampling Rate, as defined in register 25. After sampling, the latch will
          reset to the current FSYNC signal state.

          The sampled value will be reported in place of the least significant bit in
          a sensor data register determined by the value of EXT_SYNC_SET according to
          the following table.

          <pre>
          EXT_SYNC_SET | FSYNC Bit Location
          -------------+-------------------
          0            | Input disabled
          1            | TEMP_OUT_L[0]
          2            | GYRO_XOUT_L[0]
          3            | GYRO_YOUT_L[0]
          4            | GYRO_ZOUT_L[0]
          5            | ACCEL_XOUT_L[0]
          6            | ACCEL_YOUT_L[0]
          7            | ACCEL_ZOUT_L[0]
          </pre>
        :return: FSYNC configuration value
        """
        return self.read_bits(self.address, MPU6050_RA_CONFIG, MPU6050_CFG_EXT_SYNC_SET_BIT, MPU6050_CFG_EXT_SYNC_SET_LENGTH)

    def set_external_frame_sync(self, sync):
        """ Set external FSYNC configuration.

          EXT_SYNC_SET | FSYNC Bit Location
          -------------+-------------------
          0            | Input disabled
          1            | TEMP_OUT_L[0]
          2            | GYRO_XOUT_L[0]
          3            | GYRO_YOUT_L[0]
          4            | GYRO_ZOUT_L[0]
          5            | ACCEL_XOUT_L[0]
          6            | ACCEL_YOUT_L[0]
          7            | ACCEL_ZOUT_L[0]

        :param sync: value to set for sync (0-7)
        """
        self.write_bits(self.address, MPU6050_RA_CONFIG, MPU6050_CFG_EXT_SYNC_SET_BIT, MPU6050_CFG_EXT_SYNC_SET_LENGTH, sync)

    def get_dlpf_mode(self):
        """  Get digital low-pass filter configuration.

          The DLPF_CFG parameter sets the digital low pass filter configuration. It
          also determines the internal sampling rate used by the device as shown in
          the table below.

          Note: The accelerometer output rate is 1kHz. This means that for a Sample
          Rate greater than 1kHz, the same accelerometer sample may be output to the
          FIFO, DMP, and sensor registers more than once.

          <pre>
                   |   ACCELEROMETER    |           GYROSCOPE
          DLPF_CFG | Bandwidth | Delay  | Bandwidth | Delay  | Sample Rate
          ---------+-----------+--------+-----------+--------+-------------
          0        | 260Hz     | 0ms    | 256Hz     | 0.98ms | 8kHz
          1        | 184Hz     | 2.0ms  | 188Hz     | 1.9ms  | 1kHz
          2        | 94Hz      | 3.0ms  | 98Hz      | 2.8ms  | 1kHz
          3        | 44Hz      | 4.9ms  | 42Hz      | 4.8ms  | 1kHz
          4        | 21Hz      | 8.5ms  | 20Hz      | 8.3ms  | 1kHz
          5        | 10Hz      | 13.8ms | 10Hz      | 13.4ms | 1kHz
          6        | 5Hz       | 19.0ms | 5Hz       | 18.6ms | 1kHz
          7        |   -- Reserved --   |   -- Reserved --   | Reserved
          </pre>
        :return: DLFP configuration
        """
        return self.read_bits(self.address, MPU6050_RA_CONFIG, MPU6050_CFG_DLPF_CFG_BIT, MPU6050_CFG_DLPF_CFG_LENGTH)

    def set_dlpf_mode(self, mode):
        """ Set digital low-pass filter configuration.

                   |   ACCELEROMETER    |           GYROSCOPE
          DLPF_CFG | Bandwidth | Delay  | Bandwidth | Delay  | Sample Rate
          ---------+-----------+--------+-----------+--------+-------------
          0        | 260Hz     | 0ms    | 256Hz     | 0.98ms | 8kHz
          1        | 184Hz     | 2.0ms  | 188Hz     | 1.9ms  | 1kHz
          2        | 94Hz      | 3.0ms  | 98Hz      | 2.8ms  | 1kHz
          3        | 44Hz      | 4.9ms  | 42Hz      | 4.8ms  | 1kHz
          4        | 21Hz      | 8.5ms  | 20Hz      | 8.3ms  | 1kHz
          5        | 10Hz      | 13.8ms | 10Hz      | 13.4ms | 1kHz
          6        | 5Hz       | 19.0ms | 5Hz       | 18.6ms | 1kHz
          7        |   -- Reserved --   |   -- Reserved --   | Reserved

        :param mode: value to set for dlpf mode (0-6)
        :return:
        """
        self.write_bits(self.address, MPU6050_RA_CONFIG, MPU6050_CFG_DLPF_CFG_BIT, MPU6050_CFG_DLPF_CFG_LENGTH, mode)

    def get_temp(self):
        """Reads the temperature from the onboard temperature sensor of the MPU-6050.

        Returns the temperature in degrees Celcius.
        """
        raw_temp = self.read_i2c_word_data(MPU6050_RA_TEMP_OUT_H)

        # Get the actual temperature using the formule given in the
        # MPU-6050 Register Map and Descriptions revision 4.2, page 30
        actual_temp = (raw_temp / 340.0) + 36.53

        return actual_temp

    def set_accel_range(self, accel_range):
        """Sets the range of the accelerometer to range.

        accel_range -- the range to set the accelerometer to. Using a
        pre-defined range is advised.
        """
        # First change it to 0x00 to make sure we write the correct value later
        self.write_bits(self.address, MPU6050_RA_ACCEL_CONFIG, MPU6050_ACONFIG_AFS_SEL_BIT, MPU6050_ACONFIG_AFS_SEL_LENGTH, 0x00)

        # Write the new range to the ACCEL_CONFIG register
        #* The parameter allows setting the full-scale range of the accelerometer
        #* sensors, as described in the table below.
        #*
        #* 0 = +/- 2g
        #* 1 = +/- 4g
        #* 2 = +/- 8g
        #* 3 = +/- 16g

        self.write_bits(self.address, MPU6050_RA_ACCEL_CONFIG, MPU6050_ACONFIG_AFS_SEL_BIT, MPU6050_ACONFIG_AFS_SEL_LENGTH, accel_range)

    def read_accel_range(self, raw = False):
        """Reads the range the accelerometer is set to.

        If raw is True, it will return the raw value from the ACCEL_CONFIG
        register
        If raw is False, it will return an integer: -1, 2, 4, 8 or 16. When it
        returns -1 something went wrong.
        """
        raw_data = self.read_bits(self.address, MPU6050_RA_ACCEL_CONFIG, MPU6050_ACONFIG_AFS_SEL_BIT, MPU6050_ACONFIG_AFS_SEL_LENGTH)

        if raw is True:
            return raw_data
        elif raw is False:
            if raw_data == MPU6050_ACCEL_FS_2:
                return 2
            elif raw_data == MPU6050_ACCEL_FS_4:
                return 4
            elif raw_data == MPU6050_ACCEL_FS_8:
                return 8
            elif raw_data == MPU6050_ACCEL_FS_16:
                return 16
            else:
                return -1

    def get_accel_data(self, g = False, ofXacc = 0, ofYacc = 0, ofZacc = 0):
        """Gets and returns the X, Y and Z values from the accelerometer.

        If g is True, it will return the data in g
        If g is False, it will return the data in m/s^2
        Returns a dictionary with the measurement results.
        """
        x = self.read_i2c_word_data(MPU6050_RA_ACCEL_XOUT_H) + ofXacc
        y = self.read_i2c_word_data(MPU6050_RA_ACCEL_YOUT_H) + ofYacc
        z = self.read_i2c_word_data(MPU6050_RA_ACCEL_ZOUT_H) + ofZacc

        accel_scale_modifier = None
        accel_range = self.read_accel_range(True)

        if accel_range == MPU6050_ACCEL_FS_2:
            accel_scale_modifier = self.ACCEL_SCALE_MODIFIER_2G
        elif accel_range == MPU6050_ACCEL_FS_4:
            accel_scale_modifier = self.ACCEL_SCALE_MODIFIER_4G
        elif accel_range == MPU6050_ACCEL_FS_8:
            accel_scale_modifier = self.ACCEL_SCALE_MODIFIER_8G
        elif accel_range == MPU6050_ACCEL_FS_16:
            accel_scale_modifier = self.ACCEL_SCALE_MODIFIER_16G
        else:
            print("Unkown range - accel_scale_modifier set to self.ACCEL_SCALE_MODIFIER_2G")
            accel_scale_modifier = self.ACCEL_SCALE_MODIFIER_2G

        x = x / accel_scale_modifier
        y = y / accel_scale_modifier
        z = z / accel_scale_modifier

        if g is True:
            return {'x': x, 'y': y, 'z': z}
        elif g is False:
            x = x * self.GRAVITIY_MS2
            y = y * self.GRAVITIY_MS2
            z = z * self.GRAVITIY_MS2
            return {'x': x, 'y': y, 'z': z}

    def set_gyro_range(self, gyro_range):
        """Sets the range of the gyroscope to range.

        gyro_range -- the range to set the gyroscope to. Using a pre-defined
        range is advised.
        0 = +/- 250 d/sec
        1 = +/- 500 d/sec
        2 = +/- 1000 d/sec
        3 = +/- 2000 d/sec
        """
        # First change it to 0x00 to make sure we write the correct value later
        self.write_bits(self.address, MPU6050_RA_GYRO_CONFIG, MPU6050_GCONFIG_FS_SEL_BIT, MPU6050_GCONFIG_FS_SEL_LENGTH, 0x00)

        # Write the new range to the GYRO_CONFIG register
        self.write_bits(self.address, MPU6050_RA_GYRO_CONFIG, MPU6050_GCONFIG_FS_SEL_BIT, MPU6050_GCONFIG_FS_SEL_LENGTH, gyro_range)

    def read_gyro_range(self, raw = False):
        """Reads the range the gyroscope is set to.

        If raw is True, it will return the raw value from the GYRO_CONFIG
        register.
        If raw is False, it will return 250, 500, 1000, 2000 or -1. If the
        returned value is equal to -1 something went wrong.
        """
        raw_data = self.read_bits(self.address, MPU6050_RA_GYRO_CONFIG, MPU6050_GCONFIG_FS_SEL_BIT, MPU6050_GCONFIG_FS_SEL_LENGTH)

        if raw is True:
            return raw_data
        elif raw is False:
            if raw_data == MPU6050_GYRO_FS_250:
                return 250
            elif raw_data == MPU6050_GYRO_FS_500:
                return 500
            elif raw_data == MPU6050_GYRO_FS_1000:
                return 1000
            elif raw_data == MPU6050_GYRO_FS_2000:
                return 2000
            else:
                return -1

    def get_gyro_data(self):
        """Gets and returns the X, Y and Z values from the gyroscope.

        Returns the read values in a dictionary.
        """
        x = self.read_i2c_word_data(MPU6050_RA_GYRO_XOUT_H)
        y = self.read_i2c_word_data(MPU6050_RA_GYRO_YOUT_H)
        z = self.read_i2c_word_data(MPU6050_RA_GYRO_ZOUT_H)

        gyro_scale_modifier = None
        gyro_range = self.read_gyro_range(True)

        if gyro_range == MPU6050_GYRO_FS_250:
            gyro_scale_modifier = self.GYRO_SCALE_MODIFIER_250DEG
        elif gyro_range == MPU6050_GYRO_FS_500:
            gyro_scale_modifier = self.GYRO_SCALE_MODIFIER_500DEG
        elif gyro_range == MPU6050_GYRO_FS_1000:
            gyro_scale_modifier = self.GYRO_SCALE_MODIFIER_1000DEG
        elif gyro_range == MPU6050_GYRO_FS_2000:
            gyro_scale_modifier = self.GYRO_SCALE_MODIFIER_2000DEG
        else:
            print("Unkown range - gyro_scale_modifier set to self.GYRO_SCALE_MODIFIER_250DEG")
            gyro_scale_modifier = self.GYRO_SCALE_MODIFIER_250DEG

        x = x / gyro_scale_modifier
        y = y / gyro_scale_modifier
        z = z / gyro_scale_modifier

        return {'x': x, 'y': y, 'z': z}

    def get_all_data(self):
        """Reads and returns all the available data."""
        temp = self.get_temp()
        accel = self.get_accel_data()
        gyro = self.get_gyro_data()

        return [accel, gyro, temp]


if __name__ == "__main__":
    mpu = mpu6050(0x68)
    print(mpu.get_temp())
    accel_data = mpu.get_accel_data()
    print(accel_data['x'])
    print(accel_data['y'])
    print(accel_data['z'])
    gyro_data = mpu.get_gyro_data()
    print(gyro_data['x'])
    print(gyro_data['y'])
    print(gyro_data['z'])
