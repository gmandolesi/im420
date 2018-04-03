################################################################################
# Automatically-generated file. Do not edit!
################################################################################

# Add inputs and outputs from these tool invocations to the build variables 
C_SRCS += \
../Generated_Code/Cpu.c \
../Generated_Code/Task1.c \
../Generated_Code/Task2.c \
../Generated_Code/clockMan1.c \
../Generated_Code/free_rtos.c \
../Generated_Code/gpio1.c \
../Generated_Code/hardware_init.c \
../Generated_Code/osa1.c \
../Generated_Code/pin_init.c 

OBJS += \
./Generated_Code/Cpu.o \
./Generated_Code/Task1.o \
./Generated_Code/Task2.o \
./Generated_Code/clockMan1.o \
./Generated_Code/free_rtos.o \
./Generated_Code/gpio1.o \
./Generated_Code/hardware_init.o \
./Generated_Code/osa1.o \
./Generated_Code/pin_init.o 

C_DEPS += \
./Generated_Code/Cpu.d \
./Generated_Code/Task1.d \
./Generated_Code/Task2.d \
./Generated_Code/clockMan1.d \
./Generated_Code/free_rtos.d \
./Generated_Code/gpio1.d \
./Generated_Code/hardware_init.d \
./Generated_Code/osa1.d \
./Generated_Code/pin_init.d 


# Each subdirectory must supply rules for building sources it contributes
Generated_Code/%.o: ../Generated_Code/%.c
	@echo 'Building file: $<'
	@echo 'Invoking: Cross ARM C Compiler'
	arm-none-eabi-gcc -mcpu=cortex-m0plus -mthumb -O0 -fmessage-length=0 -fsigned-char -ffunction-sections -fdata-sections  -g3 -D"CPU_MKL25Z128VLK4" -D"FSL_RTOS_FREE_RTOS" -I"D:/IM420O/LAB1/SDK/platform/hal/inc" -I"D:/IM420O/LAB1/SDK/platform/hal/src/sim/MKL25Z4" -I"D:/IM420O/LAB1/SDK/platform/system/src/clock/MKL25Z4" -I"D:/IM420O/LAB1/SDK/platform/system/inc" -I"D:/IM420O/LAB1/SDK/platform/osa/inc" -I"D:/IM420O/LAB1/SDK/platform/CMSIS/Include" -I"D:/IM420O/LAB1/SDK/platform/devices" -I"D:/IM420O/LAB1/SDK/platform/devices/MKL25Z4/include" -I"D:/IM420O/LAB1/SDK/platform/devices/MKL25Z4/startup" -I"D:/IM420O/LAB1/Generated_Code/SDK/platform/devices/MKL25Z4/startup" -I"D:/IM420O/LAB1/Sources" -I"D:/IM420O/LAB1/Generated_Code" -I"D:/IM420O/LAB1/SDK/rtos/FreeRTOS/include" -I"D:/IM420O/LAB1/SDK/rtos/FreeRTOS/port/gcc" -I"D:/IM420O/LAB1/Generated_Code/SDK/rtos/FreeRTOS/config" -I"D:/IM420O/LAB1/SDK/platform/drivers/inc" -std=c99 -MMD -MP -MF"$(@:%.o=%.d)" -MT"$@" -c -o "$@" "$<"
	@echo 'Finished building: $<'
	@echo ' '


