MODULE=sc_alu

.PHONY:sim
sim: waveform.vcd

.PHONY:verilate
verilate: .stamp.verilate

.PHONY:build
build: obj_dir/V$(MODULE)

.PHONY:waveform
waveform: waveform.vcd
	@echo
	@echo "### WAVEFORM ###"
	gtkwave waveform.vcd

waveform.vcd: ./obj_dir/V$(MODULE)
	@echo
	@echo "### SIMULATING ###"
	@./obj_dir/V$(MODULE)
	@echo "### COMPLETED SIMULATION ###"

./obj_dir/V$(MODULE): .stamp.verilate
	@echo
	@echo "### BUILDING SIM ###"
	make -C obj_dir -f V$(MODULE).mk V$(MODULE)

.stamp.verilate: core/$(MODULE).v tb/tb_$(MODULE).cpp
	@echo
	@echo "### VERILATING ###"
	verilator -Wall --trace -cc core/$(MODULE).v -Icore --exe tb/tb_$(MODULE).cpp
	@touch .stamp.verilate

.PHONY:lint
lint: core/$(MODULE).v
	verilator --lint-only core/$(MODULE).v

.PHONY: clean
clean:
	rm -rf .stamp.*;
	rm -rf ./obj_dir
	rm -rf waveform.vcd
