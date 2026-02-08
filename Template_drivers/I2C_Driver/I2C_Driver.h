#ifndef I2C_H
#define I2C_H

#include "Global_Types.h"
/* ================================
 * Types & enums
 * ================================ */

typedef enum {
    I2C_OK = 0,
    I2C_ERROR,
    I2C_NACK,
    I2C_ARB_LOST,
    I2C_BUS_BUSY,
    I2C_TIMEOUT
} i2c_status_t;

typedef enum {
    I2C_SLAVE_EVT_NONE = 0,
    I2C_SLAVE_EVT_ADDR_MATCH,
    I2C_SLAVE_EVT_RX,
    I2C_SLAVE_EVT_TX,
    I2C_SLAVE_EVT_STOP,
    I2C_SLAVE_EVT_NACK
} i2c_slave_event_t;

/* ================================
 * Core control
 * ================================ */

void i2c_init(uint32_t scl_hz);
void i2c_enable(void);
void i2c_disable(void);
void i2c_reset(void);

/* ================================
 * Bus control
 * ================================ */

void i2c_generate_start(void);
void i2c_generate_stop(void);

void i2c_ack_enable(void);
void i2c_ack_disable(void);

/* ================================
 * Status & error handling
 * ================================ */

uint32_t      i2c_get_status(void);
boolean_t          i2c_bus_busy(void);
i2c_status_t  i2c_get_error(void);
void          i2c_clear_errors(void);

/* ================================
 * Data primitives
 * ================================ */

void     i2c_write_byte(uint8_t byte);
uint8_t  i2c_read_byte(void);

boolean_t     i2c_tx_ready(void);
boolean_t     i2c_rx_ready(void);

/* ================================
 * Master mode API
 * ================================ */

i2c_status_t i2c_master_write(
    uint8_t addr,
    const uint8_t *data,
    size_t len
);

i2c_status_t i2c_master_read(
    uint8_t addr,
    uint8_t *data,
    size_t len
);

i2c_status_t i2c_master_write_read(
    uint8_t addr,
    const uint8_t *tx_data,
    size_t tx_len,
    uint8_t *rx_data,
    size_t rx_len
);

/* ================================
 * Slave mode API
 * ================================ */

void i2c_slave_set_address(uint8_t own_addr);
void i2c_slave_enable(void);
void i2c_slave_disable(void);

void     i2c_slave_write_byte(uint8_t byte);
uint8_t  i2c_slave_read_byte(void);

i2c_slave_event_t i2c_slave_get_event(void);

/* ================================
 * Interrupt support
 * ================================ */

void i2c_irq_enable(void);
void i2c_irq_disable(void);
void i2c_irq_handler(void);

/* ================================
 * Bus recovery
 * ================================ */

void i2c_bus_recover(void);

#endif /* I2C_H */
