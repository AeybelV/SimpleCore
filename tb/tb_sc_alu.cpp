#include <stdlib.h>
#include <time.h>
#include <iostream>
#include <verilated.h>
#include <verilated_vcd_c.h>
#include "Vsc_alu.h"

#define MAX_SIM_TIME 225

#define SC_ALU_ADD  0
#define SC_ALU_SUB  1
#define SC_ALU_AND  2
#define SC_ALU_OR   3
#define SC_ALU_XOR  4
#define SC_ALU_SLL  5
#define SC_ALU_SRL  6
#define SC_ALU_SRA  7

vluint64_t sim_time = 0;

inline uint32_t get_alu_op(){
    if(sim_time < 25){
        return SC_ALU_ADD;
    }
    else if (sim_time < 50) {
        return SC_ALU_SUB;
    }
    else if(sim_time < 75){
        return SC_ALU_AND;
    }
    else if(sim_time < 100){
        return SC_ALU_OR;
    }
    else if(sim_time < 125){
        return SC_ALU_XOR;
    }
    else if(sim_time < 150){
        return SC_ALU_SLL;
    }
    else if(sim_time < 175){
        return SC_ALU_SRL;
    }
    else if(sim_time <= 200){
        return SC_ALU_SRA;
    }
}

int main(int argc, char** argv, char** env) {
    srand(time(0));
    Vsc_alu *dut = new Vsc_alu;

    Verilated::traceEverOn(true);
    VerilatedVcdC *m_trace = new VerilatedVcdC;
    dut->trace(m_trace, 5);
    m_trace->open("waveform.vcd");
    
    std::cout << "\n\n[SimpleCore ALU Verilator Testbench]\n\n";
    uint32_t operation = 0;
    while (sim_time < MAX_SIM_TIME) {
        
        operation = get_alu_op();

        uint32_t input_a = rand();
        uint32_t input_b = rand();
        if(operation >= SC_ALU_SLL){
            input_b = rand() % 32;
        }
        uint32_t expected;

        switch (operation) {
            case SC_ALU_ADD:{
                expected = input_a + input_b;
                break;
            }
            case SC_ALU_SUB:{
                expected = input_b - input_a;
                break;
            }
            case SC_ALU_AND:{
                expected = input_a & input_b;
                break;
            }
            case SC_ALU_OR: {
                expected = input_a | input_b;
                break;
            }
            case SC_ALU_XOR: {
                expected = input_a ^ input_b;
                break;
            }
            case SC_ALU_SLL:{
                expected = input_a << input_b;
                break;
            }
            case SC_ALU_SRL:{
                expected = input_a >> input_b;
                break;
            }
            case SC_ALU_SRA: {
                expected = (unsigned int)((unsigned int) input_a >> (unsigned int) input_b);
                break;
            }
            default:{
                expected = input_a + input_b;
                break;
            };
        };

        dut->clk ^= 1;
        
        if(dut->clk){
            dut->alu_op_in = operation;
            dut->alu_a_in = input_a;
            dut->alu_b_in = input_b;
        }
        
        dut->eval();

        if(dut->alu_out != expected && dut->clk && sim_time)
            std::cout << "["<< sim_time << "]" << "[ALU Error] Inputs (" << input_a << "," << input_b << ") Expected: " << expected << " Instead: " << dut->alu_out << std::endl;


        m_trace->dump(sim_time);
        sim_time++;
    }

    std::cout << "\n\n[SimpleCore ALU Verilator Testbench Complete]\n\n";
    m_trace->close();
    delete dut;
    exit(EXIT_SUCCESS);
}
