/* ###################################################################
**     Filename    : os_tasks.c
**     Project     : LAB1
**     Processor   : MKL25Z128VLK4
**     Component   : Events
**     Version     : Driver 01.00
**     Compiler    : GNU C Compiler
**     Date/Time   : 2018-03-06, 15:51, # CodeGen: 2
**     Abstract    :
**         This is user's event module.
**         Put your event handler code here.
**     Settings    :
**     Contents    :
**         Task1_task - void Task1_task(os_task_param_t task_init_data);
**
** ###################################################################*/
/*!
** @file os_tasks.c
** @version 01.00
** @brief
**         This is user's event module.
**         Put your event handler code here.
*/         
/*!
**  @addtogroup os_tasks_module os_tasks module documentation
**  @{
*/         
/* MODULE os_tasks */

#include "Cpu.h"
#include "Events.h"
#include "os_tasks.h"

#ifdef __cplusplus
extern "C" {
#endif 


/* User includes (#include below this line is not maintained by Processor Expert) */

/*
** ===================================================================
**     Event       :  Task1_task (module os_tasks)
**
**     Component   :  Task1 [OS_Task]
*/
/*!
**     @brief
**         RTOS task routine. The routine is generated into os_tasks.c
**         file.
**     @param
**         task_init_data  - Parameter to be passed to the
**         task when it is created.
*/
/* ===================================================================*/
void Task1_task(os_task_param_t task_init_data)
{
  /* Write your local variable definition here */
  
#ifdef PEX_USE_RTOS
  while (1) {
#endif
    /* Write your code here ... */
	  ledrgb_setGreenLed();
	  OSA_TimeDelay(1000);                 /* Example code (for task release) */

	  ledrgb_clearGreenLed();

	  OSA_TimeDelay(500);                 /* Example code (for task release) */

    
    
#ifdef PEX_USE_RTOS   
  }
#endif    
}

/*
** ===================================================================
**     Event       :  Task2_task (module os_tasks)
**
**     Component   :  Task2 [OS_Task]
*/
/*!
**     @brief
**         RTOS task routine. The routine is generated into os_tasks.c
**         file.
**     @param
**         task_init_data  - Parameter to be passed to the
**         task when it is created.
*/
/* ===================================================================*/
void Task2_task(os_task_param_t task_init_data)
{
  /* Write your local variable definition here */
  
#ifdef PEX_USE_RTOS
  while (1) {
#endif
    /* Write your code here ... */
	  ledrgb_clearRedLed();
	  OSA_TimeDelay(500);                 /* Example code (for task release) */
	  ledrgb_setRedLed();

    
	  OSA_TimeDelay(1000);                 /* Example code (for task release) */

    
#ifdef PEX_USE_RTOS   
  }
#endif    
}

/* END os_tasks */

#ifdef __cplusplus
}  /* extern "C" */
#endif 

/*!
** @}
*/
/*
** ###################################################################
**
**     This file was created by Processor Expert 10.5 [05.21]
**     for the Freescale Kinetis series of microcontrollers.
**
** ###################################################################
*/
