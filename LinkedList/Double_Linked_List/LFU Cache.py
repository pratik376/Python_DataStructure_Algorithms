from collections import defaultdict, OrderedDict

class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.min_freq = 0
        self.key_to_val_freq = {}              # key -> (value, freq)
        self.freq_to_keys = defaultdict(OrderedDict)  # freq -> keys in LRU order

    def _update(self, key: int, value=None):
        val, freq = self.key_to_val_freq[key]

        if value is not None:
            val = value

        # Remove from current frequency list
        del self.freq_to_keys[freq][key]
        if not self.freq_to_keys[freq]:
            del self.freq_to_keys[freq]
            if self.min_freq == freq:
                self.min_freq += 1

        # Add to next frequency list
        freq += 1
        self.freq_to_keys[freq][key] = None
        self.key_to_val_freq[key] = (val, freq)

    def get(self, key: int) -> int:
        if key not in self.key_to_val_freq:
            return -1

        self._update(key)
        return self.key_to_val_freq[key][0]

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        if key in self.key_to_val_freq:
            self._update(key, value)
            return

        if len(self.key_to_val_freq) >= self.capacity:
            # Evict least frequently used, and least recently used within that frequency
            evict_key, _ = self.freq_to_keys[self.min_freq].popitem(last=False)
            del self.key_to_val_freq[evict_key]

            if not self.freq_to_keys[self.min_freq]:
                del self.freq_to_keys[self.min_freq]

        # Insert new key with frequency 1
        self.key_to_val_freq[key] = (value, 1)
        self.freq_to_keys[1][key] = None
        self.min_freq = 1