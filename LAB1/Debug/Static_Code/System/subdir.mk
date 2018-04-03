################################################################################
# Automatically-generated file. Do not edit!
################################################################################

# Add inputs and outputs from these tool invocations to the build variables 
C_SRCS += \
../Static_Code/System/PE_low_level_init.c 

OBJS += \
./Static_Code/System/PE_low_level_init.o 

C_DEPS += \
./Static_Code/System/PE_low_level_init.d 


# Each subdirectory must supply rules for building sources it contributes
Static_Code/System/%.o: ../Static_Code/System/%.c
	@echo 'Building file: $<'
	@echo 'Invoking: Cross ARM C Compiler'
	arm-none-eabi-gcc -mcpu=cortex-m0plus -mthumb -O0 -fmessage-length=0 -fsigned-char -ffunction-sections -fdata-sections  -g3 -D"CPU_MKL25Z128VLK4" -D"FSL_RTOS_FREE_RTOS" -I"D:/IM420O/LAB1/SDK/platform/hal/inc" -I"D:/IM420O/LAB1/SDK/platform/hal/src/sim/MKL25Z4" -I"D:/IM420O/LAB1/SDK/platform/system/src/clock/MKL25Z4" -I"D:/IM420O/LAB1/SDK/platform/system/inc" -I"D:/IM420O/LAB1/SDK/platform/osa/inc" -I"D:/IM420O/LAB1/SDK/platform/CMSIS/Include" -I"D:/IM420O/LAB1/SDK/platform/devices" -I"D:/IM420O/LAB1/SDK/platform/devices/MKL25Z4/include" -I"D:/IM420O/LAB1/SDK/platform/devices/MKL25Z4/startup" -I"D:/IM420O/LAB1/Generated_Code/SDK/platform/devices/MKL25Z4/startup" -I"D:/IM420O/LAB1/Sources" -I"D:/IM420O/LAB1/Generated_Code" -I"D:/IM420O/LAB1/SDK/rtos/FreeRTOS/include" -I"D:/IM420O/LAB1/SDK/rtos/FreeRTOS/port/gcc" -I"D:/IM420O/LAB1/Generated_Code/SDK/rtos/FreeRTOS/config" -I"D:/IM420O/LAB1/SDK/platform/drivers/inc" -std=c99 -MMD -MP -MF"$(@:%.o=%.d)" -MT"$@" -c -o "$@" "$<"
	@echo 'Finished building: $<'
	@echo ' '


