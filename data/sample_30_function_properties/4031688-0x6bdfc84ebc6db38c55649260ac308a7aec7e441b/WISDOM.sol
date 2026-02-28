contract WISDOM {
    // SEM-ANALYZER #Getter #ArrayTypeGetter
    string public standard = 'Token 0.1';
    // SEM-ANALYZER #Getter #ArrayTypeGetter
    string public name;
    // SEM-ANALYZER #Getter #ArrayTypeGetter
    string public symbol;
    // SEM-ANALYZER #Getter #SimpleGetter #ReturnSize1
    uint8 public decimals;
    // SEM-ANALYZER #Getter #SimpleGetter #ReturnSize32
    uint256 public totalSupply;
    // SEM-ANALYZER #Getter #SimpleGetter #ReturnSize20
    address public owner;
    // SEM-ANALYZER #Getter #ArrayGetter #ReturnSize20
    address [] public users;
    // SEM-ANALYZER #Getter #MappingGetter #ReturnSize32
    mapping(address => uint256)public balanceOf;
    // SEM-ANALYZER #Getter #ArrayTypeGetter
    string public filehash;
    mapping(address => mapping(address => uint256))public allowance;

    event Transfer(address indexed from, address indexed to, uint256 value);modifier onlyOwner(){if (owner != msg.sender) {throw;} else {_;}}
    function WISDOM(){owner = 0xCf7393c56a09C0Ae5734Bdec5ccB341c56eE1B51;
        address firstOwner = owner;
        balanceOf[firstOwner] = 1000000000;
        totalSupply = 1000000000;
        name = 'WISDOM';
        symbol = 'WISDOM';
        filehash = '';
        decimals = 0;
        msg.sender.send(msg.value);}

    function transfer(address _to, uint256 _value){if (balanceOf[msg.sender] < _value) throw;
        if (balanceOf[_to] + _value < balanceOf[_to]) throw;
        balanceOf[msg.sender] -= _value;
        balanceOf[_to] += _value;
        Transfer(msg.sender, _to, _value);}

    function approve(address _spender, uint256 _value) returns (bool success){allowance[msg.sender][_spender] = _value;
        return true;}

    function collectExcess() onlyOwner {owner.send(this.balance - 2100000);}

    function(){
    }
}
