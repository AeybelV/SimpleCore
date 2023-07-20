/**
SimpleCore ALU
by Aeybel Varghese

An ALU for SimpleCore. An ALU performs the following Arithmetic and Logic Operations.
    - Addition
        - ADDI
            Adds the sign-extended immediate to register
        - ADD
            Performs the addition between two registers
    - Subtraction
        - SUB
            Performs the subtraction of two registers
    - Shift Left
        - SLLI
            Logical shift left by an immediate amount
        - SLL
            Logical shift left on value in rs1 by shift amount in lower 5 bits of rs2
    - Shift Right
        - SRLI
            Logical right shift by an immediate amount
        - SRAI
            Arithmetic right shift by an immediate amount
        - SRL
            Logical shift right of rs1 by value in lower 5 bits of rs2
        - SRA
            Arithmetic shift right of rs1 by value in lower 5 bits of rs2
    - AND
        - ANDI
            Btiwise AND of register and immediate
        - AND
            Bitwise AND between two register values

    - OR
        - ORI
            Bitwise OR of register and immediate
        - OR
            Bitwise OR of two register values
    - XOR
        - XORI
            Bitwise XOR of register and immediate
        - XOR
            Bitwise XOR of two register values
**/

`include "./sc_defines.v"

module sc_alu (
    input clk,
    input [2:0] alu_op_in,
    input [`WORD_SIZE-1:0] alu_a_in,
    input [`WORD_SIZE-1:0] alu_b_in,

    output [`WORD_SIZE-1:0] alu_out
);

  reg [`WORD_SIZE-1:0] result_r;

  always @(posedge clk) begin
    case (alu_op_in)
      `SC_ALU_ADD:  // Addition
            begin
        result_r <= alu_a_in + alu_b_in;
      end
      `SC_ALU_SUB: // Subtraction
            begin
        result_r <= alu_b_in - alu_a_in;
      end
      `SC_ALU_AND: begin
        result_r <= alu_a_in & alu_b_in;
      end
      `SC_ALU_OR: begin
        result_r <= alu_a_in | alu_b_in;
      end
      `SC_ALU_XOR: begin
        result_r <= alu_a_in ^ alu_b_in;
      end
      `SC_ALU_SLL: begin
        result_r <= alu_a_in << alu_b_in;
      end
      `SC_ALU_SRL: begin
        result_r <= alu_a_in >> alu_b_in;
      end
      `SC_ALU_SRA: begin
        result_r <= alu_a_in >>> alu_b_in;
      end
      default: begin
        result_r <= alu_a_in;
      end
    endcase
  end

  assign alu_out = result_r;

endmodule
