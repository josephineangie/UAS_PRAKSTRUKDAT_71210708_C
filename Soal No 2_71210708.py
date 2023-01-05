class Node:
 def __init__(self,data,priority):
    self._data = data
    self._priority = priority
    self._next = None
    self._prev = None
    
class PQSTugas:
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def isEmpty(self):
        if self._size == 0:
            return True
        else:
            return False

    def printAll(self):
        if self.isEmpty() == True:
            print("Sudah tidak ada tugas yang bisa dihapus.")
        else:
            bantu = self._head
            while bantu != None:
                print ("(", bantu._data, ",", bantu._priority, ")", end="")
                bantu = bantu._next
                print()


    def _addHead(self, newNode):
        #isi kode anda
        pass

    def _addTail(self, newNode):
        #isi kode anda
        pass

    def _addMiddle(self, newNode):
        #isi kode anda
        pass

    def add(self, data, priority):
        # data = [int(priority), data]
        # self._data.append(data)
        # self._data.sort()
        # self._size += 1
        baru = Node(data, priority)
        if self._isEmpty():
            self._head = baru
            self._tail = baru
        elif self._size == 1:
            if self._head._priority > priority:
                baru._next = self._head
                self._head._prev = baru
                self._head = baru
            else:
                self._head._next = baru
                baru._prev = self._head
                self._tail = baru
        else:
            if self._head._priority > priority:
                baru._next = self._head
                self._head._prev = baru
                self._tail = baru
            elif self._tail._priority <= priority:
                self._tail._next = baru
                baru._prev = self._tail
                self._tail = baru
                self._tail._next = None
            else:
                bantu = self._head
                while bantu._priority < priority:
                    bantu = bantu._next
                    bantu2 = bantu._prev
                    baru._next = bantu
                    bantu._prev = baru
                    bantu2._next = baru
                    baru._prev = bantu2
                self._size =+ 1

    def remove(self):
        if self._isEmpty () == False:
            hapus = self._head
            if self._size == 1:
                self._head = None
            else:
                self._head = self._head._next
                self._head._prev = None
            del hapus
            self._size =- 1

    def removePriority(self, priority):
        list2 = []
        for x in range (len(self._data)):
            if self._data[x][0] == n:
                del self._data[x][1]
            for y in range (len(self._data)):
                if len(self._data[y]) == 1:
                    pass
                else:
                    list2.append(self._data[y]) 
            self._data = list2
            self._size -= 1


if __name__ == "__main__":
    tugasKu = PQSTugas()
    tugasKu.add("StrukDat",1)
    tugasKu.add("Menyapu", 5)
    tugasKu.add("Cuci Baju", 4)
    tugasKu.add("Beli Alat Tulis", 3)
    tugasKu.add("Cuci Sepatu", 4)
    tugasKu.printAll()
    tugasKu.remove()
    tugasKu.printAll()
    tugasKu.removePriority(2)
    tugasKu.removePriority(4)
    tugasKu.printtAll()