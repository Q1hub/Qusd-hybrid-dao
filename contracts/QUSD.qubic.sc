// contracts/QUSD.qubic.sc
public name = "Qubic USD"
public symbol = "QUSD"
public decimals = 6
public totalSupply = 0

mapping(address => uint64) balanceOf
mapping(address => bool) public isExecutor
address public admin = msg.sender

event Transfer(address indexed from, address indexed to, uint64 amount)
event Mint(address indexed to, uint64 amount)
event Burn(address indexed from, uint64 amount)

function mint(address to, uint64 amount) {
    require(isExecutor[msg.sender], "Not executor")
    balanceOf[to] += amount
    totalSupply += amount
    emit Transfer(0x0, to, amount)
    emit Mint(to, amount)
}

function burn(uint64 amount) {
    require(balanceOf[msg.sender] >= amount, "Insufficient")
    balanceOf[msg.sender] -= amount
    totalSupply -= amount
    emit Transfer(msg.sender, 0x0, amount)
    emit Burn(msg.sender, amount)
}

function transfer(address to, uint64 amount) {
    require(balanceOf[msg.sender] >= amount, "Insufficient")
    balanceOf[msg.sender] -= amount
    balanceOf[to] += amount
    emit Transfer(msg.sender, to, amount)
}

// Admin / DAO functions
function addExecutor(address exec) { require(msg.sender == admin); isExecutor[exec] = true; }
function removeExecutor(address exec) { require(msg.sender == admin); isExecutor[exec] = false; }
function transferAdmin(address newAdmin) { require(msg.sender == admin); admin = newAdmin; }
